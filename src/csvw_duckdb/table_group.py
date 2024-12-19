import csvw.db


class TableGroup:
    """
    A a group of tables, which are data structure made of a collection of rows and columns.
    https://www.w3.org/ns/csvw#class-definitions
    """

    def __init__(self, path):
        """
        :param table: CSVW table definition https://www.w3.org/ns/csvw#class-definitions
        """
        self.path = path
        self.table_group = csvw.TableGroup.from_file(path)
        self.database = csvw.db.Database(self.table_group)

    def iter_sql(self):
        for table in self.database.tables:
            yield table.sql(translate=self.database.translate) + ';'
