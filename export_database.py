from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session as SessionType
import pandas as pd
from dotenv import load_dotenv
import os
from typing import Optional

# Load environment variables
load_dotenv()
DATABASE_USER: Optional[str] = os.getenv("DATABASE_USER")
DATABASE_PASSWORD: Optional[str] = os.getenv("DATABASE_PASSWORD")
HOST_NAME: Optional[str] = os.getenv("HOSTNAME")
DATABASE_URL: str = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{HOST_NAME}:5432/ecoactdb"

# Define the ORM mapping
Base = declarative_base()

class ElementData(Base):
    """
    Class SQLAlchemy ORM model for the ecoact elemenent data table.

    Attributes:
        id (Integer): Primary key, auto-incremented.
        All other fields match the columns provided.
    """

    __tablename__: str = 'element_data'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    type_ligne: Optional[str] = Column(String)
    identifiant_element: Optional[float] = Column(Float)
    structure: Optional[str] = Column(String)
    statut_element: Optional[str] = Column(String)
    nom_base_francais: Optional[str] = Column(String)
    nom_attribut_francais: Optional[str] = Column(String)
    nom_frontiere_francais: Optional[str] = Column(String)
    code_categorie: Optional[str] = Column(String)
    tags_francais: Optional[str] = Column(String)
    unite_francais: Optional[str] = Column(String)
    contributeur: Optional[str] = Column(String)
    programme: Optional[str] = Column(String)
    url_programme: Optional[str] = Column(Text)
    source: Optional[str] = Column(String)
    localisation_geo: Optional[str] = Column(String)
    sous_localisation_geo_francais: Optional[str] = Column(String)
    date_creation: Optional[str] = Column(String)
    date_modification: Optional[str] = Column(String)
    periode_validite: Optional[str] = Column(String)
    incertitude: Optional[str] = Column(String)
    reglementations: Optional[str] = Column(String)
    transparence: Optional[str] = Column(String)
    qualite: Optional[str] = Column(String)
    qualite_ter: Optional[str] = Column(String)
    qualite_gr: Optional[str] = Column(String)
    qualite_tir: Optional[str] = Column(String)
    qualite_c: Optional[str] = Column(String)
    qualite_p: Optional[str] = Column(String)
    qualite_m: Optional[str] = Column(String)
    commentaire_francais: Optional[str] = Column(String)
    type_poste: Optional[str] = Column(String)
    nom_poste_francais: Optional[str] = Column(String)
    total_poste_non_decompose: Optional[float] = Column(Float)
    co2f: Optional[float] = Column(Float)
    ch4f: Optional[float] = Column(Float)
    ch4b: Optional[float] = Column(Float)
    n2o: Optional[float] = Column(Float)
    code_gaz_supplementaire_1: Optional[str] = Column(String)
    valeur_gaz_supplementaire_1: Optional[float] = Column(Float)
    code_gaz_supplementaire_2: Optional[str] = Column(String)
    valeur_gaz_supplementaire_2: Optional[float] = Column(Float)
    code_gaz_supplementaire_3: Optional[str] = Column(String)
    valeur_gaz_supplementaire_3: Optional[float] = Column(Float)
    code_gaz_supplementaire_4: Optional[str] = Column(String)
    valeur_gaz_supplementaire_4: Optional[float] = Column(Float)
    code_gaz_supplementaire_5: Optional[str] = Column(String)
    valeur_gaz_supplementaire_5: Optional[float] = Column(Float)
    autres_ges: Optional[float] = Column(Float)
    co2b: Optional[float] = Column(Float)

# Create a database connection
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session: SessionType = Session()

# Write data to the database
def write_to_database(df: pd.DataFrame) -> None:
    """
    Writes data from a DataFrame to the database.

    Args:
        df (pandas.DataFrame): DataFrame containing the data to be written to the database.

    Returns:
        None
    """
    for _, row in df.iterrows():
        element = ElementData(
            type_ligne=row.get("Type Ligne"),
            identifiant_element=row.get("Identifiant de l'élément"),
            structure=row.get("Structure"),
            statut_element=row.get("Statut de l'élément"),
            nom_base_francais=row.get("Nom base français"),
            nom_attribut_francais=row.get("Nom attribut français"),
            nom_frontiere_francais=row.get("Nom frontière français"),
            code_categorie=row.get("Code de la catégorie"),
            tags_francais=row.get("Tags français"),
            unite_francais=row.get("Unité français"),
            contributeur=row.get("Contributeur"),
            programme=row.get("Programme"),
            url_programme=row.get("Url du programme"),
            source=row.get("Source"),
            localisation_geo=row.get("Localisation géographique"),
            sous_localisation_geo_francais=row.get("Sous-localisation géographique français"),
            date_creation=row.get("Date de création"),
            date_modification=row.get("Date de modification"),
            periode_validite=row.get("Période de validité"),
            incertitude=row.get("Incertitude"),
            reglementations=row.get("Réglementations"),
            transparence=row.get("Transparence"),
            qualite=row.get("Qualité"),
            qualite_ter=row.get("Qualité TeR"),
            qualite_gr=row.get("Qualité GR"),
            qualite_tir=row.get("Qualité TiR"),
            qualite_c=row.get("Qualité C"),
            qualite_p=row.get("Qualité P"),
            qualite_m=row.get("Qualité M"),
            commentaire_francais=row.get("Commentaire français"),
            type_poste=row.get("Type poste"),
            nom_poste_francais=row.get("Nom poste français"),
            total_poste_non_decompose=row.get("Total poste non décomposé"),
            co2f=row.get("CO2f"),
            ch4f=row.get("CH4f"),
            ch4b=row.get("CH4b"),
            n2o=row.get("N2O"),
            code_gaz_supplementaire_1=row.get("Code gaz supplémentaire 1"),
            valeur_gaz_supplementaire_1=row.get("Valeur gaz supplémentaire 1"),
            code_gaz_supplementaire_2=row.get("Code gaz supplémentaire 2"),
            valeur_gaz_supplementaire_2=row.get("Valeur gaz supplémentaire 2"),
            code_gaz_supplementaire_3=row.get("Code gaz supplémentaire 3"),
            valeur_gaz_supplementaire_3=row.get("Valeur gaz supplémentaire 3"),
            code_gaz_supplementaire_4=row.get("Code gaz supplémentaire 4"),
            valeur_gaz_supplementaire_4=row.get("Valeur gaz supplémentaire 4"),
            code_gaz_supplementaire_5=row.get("Code gaz supplémentaire 5"),
            valeur_gaz_supplementaire_5=row.get("Valeur gaz supplémentaire 5"),
            autres_ges=row.get("Autres GES"),
            co2b=row.get("CO2b"),
        )
        session.add(element)
    session.commit()
