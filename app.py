import io

import joblib
import numpy as np
import pandas as pd
import streamlit as st


@st.cache_resource(show_spinner='Lade Modelle...')
def load_models():
    encoder = joblib.load('encoder.pkl')
    scaler = joblib.load('scaler.pkl')
    kmeans = joblib.load('kmeans.pkl')
    return encoder, scaler, kmeans


encoder, scaler, kmeans = load_models()

EXPECTED_FEATURES = list(scaler.feature_names_in_)
ENCODED_COLS = list(encoder.get_feature_names_out(['sexo']))
INPUT_COLS = ['sexo'] + [c for c in EXPECTED_FEATURES if c not in ENCODED_COLS]
VALID_SEXO = list(encoder.categories_[0])
GROUP_DESCRIPTIONS = {
    0: 'Fokus auf ein junges Publikum mit starkem Interesse an Mode, Musik und Aussehen.',
    1: 'Stark assoziiert mit Sport, insbesondere American Football, Basketball und kulturellen Aktivitäten wie Band und Rockmusik.',
    2: 'Ausgewogener, mit Interessen an Musik, Tanz und Mode.',
}


def validate(df: pd.DataFrame) -> list[str]:
    errors = []
    missing = [c for c in INPUT_COLS if c not in df.columns]
    if missing:
        errors.append(f'Fehlende Spalten: {missing}')
    if 'sexo' in df.columns:
        invalid = set(df['sexo'].dropna().unique()) - set(VALID_SEXO)
        if invalid:
            errors.append(f"Ungültige Werte in 'sexo': {sorted(invalid)}. Erlaubt: {VALID_SEXO}")
        if df['sexo'].isna().any():
            errors.append("Spalte 'sexo' enthält fehlende Werte.")
    numeric_cols = [c for c in INPUT_COLS if c != 'sexo' and c in df.columns]
    non_numeric = [c for c in numeric_cols if not pd.api.types.is_numeric_dtype(df[c])]
    if non_numeric:
        errors.append(f'Spalten müssen numerisch sein: {non_numeric}')
    return errors


def predict_clusters(df: pd.DataFrame) -> np.ndarray:
    encoded = encoder.transform(df[['sexo']])
    if hasattr(encoded, 'toarray'):
        encoded = encoded.toarray()
    encoded_df = pd.DataFrame(encoded, columns=ENCODED_COLS, index=df.index)
    dados = pd.concat([df.drop(columns=['sexo']), encoded_df], axis=1)
    dados = dados[EXPECTED_FEATURES]
    scaled = scaler.transform(dados)
    return kmeans.predict(scaled)


def build_template_csv() -> str:
    sample = {'sexo': ['F', 'M', 'NE']}
    for col in INPUT_COLS:
        if col == 'sexo':
            continue
        sample[col] = [16, 17, 15] if col == 'idade' else [10, 5, 0]
    return pd.DataFrame(sample)[INPUT_COLS].to_csv(index=False)


st.set_page_config(page_title='Marketing-Interessengruppen', page_icon='🎯', layout='wide')
st.title('🎯 Marketing-Interessengruppen')
st.write(
    'In diesem Projekt haben wir den K-Means-Clustering-Algorithmus angewendet, '
    'um Nutzerinteressengruppen zu identifizieren und vorherzusagen, mit dem Ziel, '
    'Marketingkampagnen effektiver auszurichten.'
)

with st.sidebar:
    st.header('📋 Erwartetes CSV-Format')
    st.write(f'**{len(INPUT_COLS)} Spalten** in dieser Reihenfolge:')
    st.code(', '.join(INPUT_COLS), language='text')
    st.write(f"**Erlaubte Werte für `sexo`:** {VALID_SEXO}")
    st.download_button(
        '⬇️ Vorlage herunterladen',
        data=build_template_csv(),
        file_name='vorlage.csv',
        mime='text/csv',
    )

up_file = st.file_uploader('Wählen Sie eine CSV-Datei für die Vorhersage aus', type='csv')

if up_file is None:
    st.info('Bitte laden Sie eine CSV-Datei hoch, um zu starten.')
    st.stop()

try:
    df = pd.read_csv(up_file)
except Exception as exc:
    st.error(f'CSV konnte nicht gelesen werden: {exc}')
    st.stop()

errors = validate(df)
if errors:
    st.error('❌ Validierung fehlgeschlagen:')
    for e in errors:
        st.write(f'- {e}')
    st.stop()

try:
    with st.spinner('Berechne Cluster...'):
        clusters = predict_clusters(df)
except Exception as exc:
    st.error(f'Fehler bei der Vorhersage: {exc}')
    st.stop()

result = df.copy()
result.insert(0, 'Gruppen', clusters)

st.success(f'✅ {len(result)} Datensätze erfolgreich klassifiziert.')

col1, col2 = st.columns([2, 1])
with col1:
    st.subheader('Verteilung')
    st.bar_chart(pd.Series(clusters).value_counts().sort_index())
with col2:
    st.subheader('Beschreibungen')
    for g, desc in GROUP_DESCRIPTIONS.items():
        st.markdown(f'**Gruppe {g}:** {desc}')

st.subheader('Ergebnisansicht (erste 10 Datensätze)')
st.dataframe(result.head(10))

buf = io.StringIO()
result.to_csv(buf, index=False)
st.download_button(
    label='⬇️ Vollständige Ergebnisse herunterladen',
    data=buf.getvalue(),
    file_name='Interessengruppen.csv',
    mime='text/csv',
)
