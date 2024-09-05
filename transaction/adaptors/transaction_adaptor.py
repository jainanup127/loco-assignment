# adaptors/transaction_adaptor.py
from transaction.dtos.transaction_dto import TransactionDTO, TransactionResponseDTO
from transaction.models.transaction import Transaction


class TransactionAdaptor:

    @staticmethod
    def dto_to_entity(dto: TransactionDTO) -> Transaction:
        """Converts DTO to a Transaction entity"""
        return Transaction(
            amount=dto.amount,
            type=dto.type,
            parent_id=dto.parent_id
        )

    @staticmethod
    def entity_to_dto(transaction: Transaction) -> TransactionResponseDTO:
        """Converts Transaction entity to a DTO"""
        if transaction:
            return TransactionResponseDTO(
                id=transaction.id,
                amount=transaction.amount,
                type=transaction.type,
                parent_id=transaction.parent_id
            )
        return
