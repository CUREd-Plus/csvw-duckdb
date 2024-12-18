class Table:
    def __init__(self, table: dict):
        self.table = table

    def to_sql(self):
        return "SELECT 1;"
