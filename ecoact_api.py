from flask import Flask, jsonify, request, abort
from sqlalchemy.orm import sessionmaker, Session as SessionType
from sqlalchemy import create_engine
from export_database import ElementData
from dotenv import load_dotenv
import os
from typing import List, Dict, Any, Optional

# Load environment variables
load_dotenv()
DATABASE_USER: Optional[str] = os.getenv("DATABASE_USER")
DATABASE_PASSWORD: Optional[str] = os.getenv("DATABASE_PASSWORD")
HOST_NAME: Optional[str] = os.getenv("HOSTNAME")
DATABASE_URL: str = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{HOST_NAME}:5432/ecoactdb"

app = Flask(__name__)

# Connection to database
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session: SessionType = Session()


@app.route('/elements', methods=['GET'])
def get_elements() -> List[Dict[str, Any]]:
    """
    Retrieve all elements from the database.

    Returns:
        List[Dict[str, Any]]: A JSON list of all elements, where each element is represented as a dictionary.
    """
    elements = session.query(ElementData).all()
    result = [
    {
        "id": element.id,
        "type_ligne": element.type_ligne,
        "identifiant_element": element.identifiant_element,
        "structure": element.structure,
        "statut_element": element.statut_element,
        "nom_base_francais": element.nom_base_francais,
        "nom_attribut_francais": element.nom_attribut_francais,
        "nom_frontiere_francais": element.nom_frontiere_francais,
        "code_categorie": element.code_categorie,
        "tags_francais": element.tags_francais,
        "unite_francais": element.unite_francais,
        "contributeur": element.contributeur,
        "programme": element.programme,
        "url_programme": element.url_programme,
        "source": element.source,
        "localisation_geo": element.localisation_geo,
        "sous_localisation_geo_francais": element.sous_localisation_geo_francais,
        "date_creation": element.date_creation,
        "date_modification": element.date_modification,
        "periode_validite": element.periode_validite,
        "incertitude": element.incertitude,
        "reglementations": element.reglementations,
        "transparence": element.transparence,
        "qualite": element.qualite,
        "qualite_ter": element.qualite_ter,
        "qualite_gr": element.qualite_gr,
        "qualite_tir": element.qualite_tir,
        "qualite_c": element.qualite_c,
        "qualite_p": element.qualite_p,
        "qualite_m": element.qualite_m,
        "commentaire_francais": element.commentaire_francais,
        "type_poste": element.type_poste,
        "nom_poste_francais": element.nom_poste_francais,
        "total_poste_non_decompose": element.total_poste_non_decompose,
        "co2f": element.co2f,
        "ch4f": element.ch4f,
        "ch4b": element.ch4b,
        "n2o": element.n2o,
        "code_gaz_supplementaire_1": element.code_gaz_supplementaire_1,
        "valeur_gaz_supplementaire_1": element.valeur_gaz_supplementaire_1,
        "code_gaz_supplementaire_2": element.code_gaz_supplementaire_2,
        "valeur_gaz_supplementaire_2": element.valeur_gaz_supplementaire_2,
        "code_gaz_supplementaire_3": element.code_gaz_supplementaire_3,
        "valeur_gaz_supplementaire_3": element.valeur_gaz_supplementaire_3,
        "code_gaz_supplementaire_4": element.code_gaz_supplementaire_4,
        "valeur_gaz_supplementaire_4": element.valeur_gaz_supplementaire_4,
        "code_gaz_supplementaire_5": element.code_gaz_supplementaire_5,
        "valeur_gaz_supplementaire_5": element.valeur_gaz_supplementaire_5,
        "autres_ges": element.autres_ges,
        "co2b": element.co2b,
    }
    for element in elements
    ]

    return jsonify(result)


@app.route('/elements/<int:id>', methods=['GET'])
def get_element_by_id(id: int) -> Dict[str, Any]:
    """
    Retrieve a specific element by its ID.

    Args:
        id (int): The ID of the element.

    Returns:
        Dict[str, Any]: A JSON representation of the requested element.

    Raises:
        404: If the element is not found in the database.
    """
    element = session.query(ElementData).get(id)
    if not element:
        abort(404, description="Element not found")
    result = {
    "id": element.id,
    "type_ligne": element.type_ligne,
    "identifiant_element": element.identifiant_element,
    "structure": element.structure,
    "statut_element": element.statut_element,
    "nom_base_francais": element.nom_base_francais,
    "nom_attribut_francais": element.nom_attribut_francais,
    "nom_frontiere_francais": element.nom_frontiere_francais,
    "code_categorie": element.code_categorie,
    "tags_francais": element.tags_francais,
    "unite_francais": element.unite_francais,
    "contributeur": element.contributeur,
    "programme": element.programme,
    "url_programme": element.url_programme,
    "source": element.source,
    "localisation_geo": element.localisation_geo,
    "sous_localisation_geo_francais": element.sous_localisation_geo_francais,
    "date_creation": element.date_creation,
    "date_modification": element.date_modification,
    "periode_validite": element.periode_validite,
    "incertitude": element.incertitude,
    "reglementations": element.reglementations,
    "transparence": element.transparence,
    "qualite": element.qualite,
    "qualite_ter": element.qualite_ter,
    "qualite_gr": element.qualite_gr,
    "qualite_tir": element.qualite_tir,
    "qualite_c": element.qualite_c,
    "qualite_p": element.qualite_p,
    "qualite_m": element.qualite_m,
    "commentaire_francais": element.commentaire_francais,
    "type_poste": element.type_poste,
    "nom_poste_francais": element.nom_poste_francais,
    "total_poste_non_decompose": element.total_poste_non_decompose,
    "co2f": element.co2f,
    "ch4f": element.ch4f,
    "ch4b": element.ch4b,
    "n2o": element.n2o,
    "code_gaz_supplementaire_1": element.code_gaz_supplementaire_1,
    "valeur_gaz_supplementaire_1": element.valeur_gaz_supplementaire_1,
    "code_gaz_supplementaire_2": element.code_gaz_supplementaire_2,
    "valeur_gaz_supplementaire_2": element.valeur_gaz_supplementaire_2,
    "code_gaz_supplementaire_3": element.code_gaz_supplementaire_3,
    "valeur_gaz_supplementaire_3": element.valeur_gaz_supplementaire_3,
    "code_gaz_supplementaire_4": element.code_gaz_supplementaire_4,
    "valeur_gaz_supplementaire_4": element.valeur_gaz_supplementaire_4,
    "code_gaz_supplementaire_5": element.code_gaz_supplementaire_5,
    "valeur_gaz_supplementaire_5": element.valeur_gaz_supplementaire_5,
    "autres_ges": element.autres_ges,
    "co2b": element.co2b,
    }

    return jsonify(result)


@app.route('/elements', methods=['POST'])
def create_element() -> (Dict[str, int], int):
    """
    Create a new element in the database.

    Returns:
        (Dict[str, int], int): A JSON object containing the ID of the created element and the HTTP status code.

    Raises:
        400: If the input data is invalid or missing.
    """
    data: Dict[str, Any] = request.json  # Input JSON data from the request
    if not data:
        abort(400, description="Invalid input")

    # Create a new element with all fields from the input
    element = ElementData(
        type_ligne=data.get("type_ligne"),
        identifiant_element=data.get("identifiant_element"),
        structure=data.get("structure"),
        statut_element=data.get("statut_element"),
        nom_base_francais=data.get("nom_base_francais"),
        nom_attribut_francais=data.get("nom_attribut_francais"),
        nom_frontiere_francais=data.get("nom_frontiere_francais"),
        code_categorie=data.get("code_categorie"),
        tags_francais=data.get("tags_francais"),
        unite_francais=data.get("unite_francais"),
        contributeur=data.get("contributeur"),
        programme=data.get("programme"),
        url_programme=data.get("url_programme"),
        source=data.get("source"),
        localisation_geo=data.get("localisation_geo"),
        sous_localisation_geo_francais=data.get("sous_localisation_geo_francais"),
        date_creation=data.get("date_creation"),
        date_modification=data.get("date_modification"),
        periode_validite=data.get("periode_validite"),
        incertitude=data.get("incertitude"),
        reglementations=data.get("reglementations"),
        transparence=data.get("transparence"),
        qualite=data.get("qualite"),
        qualite_ter=data.get("qualite_ter"),
        qualite_gr=data.get("qualite_gr"),
        qualite_tir=data.get("qualite_tir"),
        qualite_c=data.get("qualite_c"),
        qualite_p=data.get("qualite_p"),
        qualite_m=data.get("qualite_m"),
        commentaire_francais=data.get("commentaire_francais"),
        type_poste=data.get("type_poste"),
        nom_poste_francais=data.get("nom_poste_francais"),
        total_poste_non_decompose=data.get("total_poste_non_decompose"),
        co2f=data.get("co2f"),
        ch4f=data.get("ch4f"),
        ch4b=data.get("ch4b"),
        n2o=data.get("n2o"),
        code_gaz_supplementaire_1=data.get("code_gaz_supplementaire_1"),
        valeur_gaz_supplementaire_1=data.get("valeur_gaz_supplementaire_1"),
        code_gaz_supplementaire_2=data.get("code_gaz_supplementaire_2"),
        valeur_gaz_supplementaire_2=data.get("valeur_gaz_supplementaire_2"),
        code_gaz_supplementaire_3=data.get("code_gaz_supplementaire_3"),
        valeur_gaz_supplementaire_3=data.get("valeur_gaz_supplementaire_3"),
        code_gaz_supplementaire_4=data.get("code_gaz_supplementaire_4"),
        valeur_gaz_supplementaire_4=data.get("valeur_gaz_supplementaire_4"),
        code_gaz_supplementaire_5=data.get("code_gaz_supplementaire_5"),
        valeur_gaz_supplementaire_5=data.get("valeur_gaz_supplementaire_5"),
        autres_ges=data.get("autres_ges"),
        co2b=data.get("co2b"),
    )

    # Add the new element to the database
    session.add(element)
    session.commit()

    # Return the ID of the created element and a 201 HTTP status code
    return jsonify({"id": element.id}), 201

@app.route('/elements/<int:id>', methods=['PUT'])
def update_element(id: int) -> Dict[str, str]:
    """
    Update an existing element by its ID.

    Args:
        id (int): The ID of the element to update.

    Returns:
        Dict[str, str]: A JSON object confirming the update.

    Raises:
        404: If the element is not found in the database.
    """
    data: Dict[str, Any] = request.json
    element = session.query(ElementData).get(id)
    if not element:
        abort(404, description="Element not found")
    from typing import Dict, Any

    data: Dict[str, Any] = request.json  # Input data from the request
    element = session.query(ElementData).get(id)  # Fetch the element by ID

    if not element:
        abort(404, description="Element not found")

    # Update fields dynamically from the input data
    element.type_ligne = data.get("type_ligne", element.type_ligne)
    element.identifiant_element = data.get("identifiant_element", element.identifiant_element)
    element.structure = data.get("structure", element.structure)
    element.statut_element = data.get("statut_element", element.statut_element)
    element.nom_base_francais = data.get("nom_base_francais", element.nom_base_francais)
    element.nom_attribut_francais = data.get("nom_attribut_francais", element.nom_attribut_francais)
    element.nom_frontiere_francais = data.get("nom_frontiere_francais", element.nom_frontiere_francais)
    element.code_categorie = data.get("code_categorie", element.code_categorie)
    element.tags_francais = data.get("tags_francais", element.tags_francais)
    element.unite_francais = data.get("unite_francais", element.unite_francais)
    element.contributeur = data.get("contributeur", element.contributeur)
    element.programme = data.get("programme", element.programme)
    element.url_programme = data.get("url_programme", element.url_programme)
    element.source = data.get("source", element.source)
    element.localisation_geo = data.get("localisation_geo", element.localisation_geo)
    element.sous_localisation_geo_francais = data.get("sous_localisation_geo_francais", element.sous_localisation_geo_francais)
    element.date_creation = data.get("date_creation", element.date_creation)
    element.date_modification = data.get("date_modification", element.date_modification)
    element.periode_validite = data.get("periode_validite", element.periode_validite)
    element.incertitude = data.get("incertitude", element.incertitude)
    element.reglementations = data.get("reglementations", element.reglementations)
    element.transparence = data.get("transparence", element.transparence)
    element.qualite = data.get("qualite", element.qualite)
    element.qualite_ter = data.get("qualite_ter", element.qualite_ter)
    element.qualite_gr = data.get("qualite_gr", element.qualite_gr)
    element.qualite_tir = data.get("qualite_tir", element.qualite_tir)
    element.qualite_c = data.get("qualite_c", element.qualite_c)
    element.qualite_p = data.get("qualite_p", element.qualite_p)
    element.qualite_m = data.get("qualite_m", element.qualite_m)
    element.commentaire_francais = data.get("commentaire_francais", element.commentaire_francais)
    element.type_poste = data.get("type_poste", element.type_poste)
    element.nom_poste_francais = data.get("nom_poste_francais", element.nom_poste_francais)
    element.total_poste_non_decompose = data.get("total_poste_non_decompose", element.total_poste_non_decompose)
    element.co2f = data.get("co2f", element.co2f)
    element.ch4f = data.get("ch4f", element.ch4f)
    element.ch4b = data.get("ch4b", element.ch4b)
    element.n2o = data.get("n2o", element.n2o)
    element.code_gaz_supplementaire_1 = data.get("code_gaz_supplementaire_1", element.code_gaz_supplementaire_1)
    element.valeur_gaz_supplementaire_1 = data.get("valeur_gaz_supplementaire_1", element.valeur_gaz_supplementaire_1)
    element.code_gaz_supplementaire_2 = data.get("code_gaz_supplementaire_2", element.code_gaz_supplementaire_2)
    element.valeur_gaz_supplementaire_2 = data.get("valeur_gaz_supplementaire_2", element.valeur_gaz_supplementaire_2)
    element.code_gaz_supplementaire_3 = data.get("code_gaz_supplementaire_3", element.code_gaz_supplementaire_3)
    element.valeur_gaz_supplementaire_3 = data.get("valeur_gaz_supplementaire_3", element.valeur_gaz_supplementaire_3)
    element.code_gaz_supplementaire_4 = data.get("code_gaz_supplementaire_4", element.code_gaz_supplementaire_4)
    element.valeur_gaz_supplementaire_4 = data.get("valeur_gaz_supplementaire_4", element.valeur_gaz_supplementaire_4)
    element.code_gaz_supplementaire_5 = data.get("code_gaz_supplementaire_5", element.code_gaz_supplementaire_5)
    element.valeur_gaz_supplementaire_5 = data.get("valeur_gaz_supplementaire_5", element.valeur_gaz_supplementaire_5)
    element.autres_ges = data.get("autres_ges", element.autres_ges)
    element.co2b = data.get("co2b", element.co2b)

    session.commit()
    return jsonify({"message": "Element updated"})


@app.route('/elements/<int:id>', methods=['DELETE'])
def delete_element(id: int) -> Dict[str, str]:
    """
    Delete an element from the database by id.

    Args:
        id (int): The Id of the element to delete.

    Returns:
        Dict[str, str]: A JSON object confirming the deletion.

    Raises:
        404: If the element is not found in the database.
    """
    element = session.query(ElementData).get(id)
    if not element:
        abort(404, description="Element not found")
    session.delete(element)
    session.commit()
    return jsonify({"message": "Element deleted"})


if __name__ == '__main__':
    app.run(debug=True)
