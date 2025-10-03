"""
Exceptions personnalisées pour WhytDD
"""

class WhytDDException(Exception):
    """Exception de base pour WhytDD"""
    pass

class ModelNotFoundError(WhytDDException):
    """Modèle GGUF non trouvé"""
    pass

class CharacterNotFoundError(WhytDDException):
    """Personnage non trouvé"""
    pass

class InvalidCharacterDataError(WhytDDException):
    """Données de personnage invalides"""
    pass

class RAGRetrievalError(WhytDDException):
    """Erreur lors de la récupération RAG"""
    pass

class EmbeddingError(WhytDDException):
    """Erreur lors de la génération d'embeddings"""
    pass

class LLMGenerationError(WhytDDException):
    """Erreur lors de la génération GGUF"""
    pass

class ConfigurationError(WhytDDException):
    """Erreur de configuration"""
    pass
