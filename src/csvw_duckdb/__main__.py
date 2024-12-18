import argparse
import json
import logging
from pathlib import Path

from .table import Table

logger = logging.getLogger(__name__)

DESCRIPTION = """
Load a CSVW document and generate simple SQL SELECT statements.
One SQL file will be generated per table in the CSVW table group.
"""

XML_SCHEMA_TO_SQL = dict(
    string="VARCHAR",
    date="DATE",
    time="TIME",
    dateTime="TIMESTAMP",
    long="BITINT",
    integer="UBIGINT",
    float="FLOAT",
    boolean="BOOLEAN",
    double="DOUBLE",
    decimal="DECIMAL",
)
"""
https://www.w3.org/2001/sw/rdb2rdf/wiki/Mapping_SQL_datatypes_to_XML_Schema_datatypes
Map from XML Schema data types https://www.w3.org/TR/xmlschema-2/#typesystem
to DuckDB SQL data types https://duckdb.org/docs/sql/data_types/overview.html
"""


def get_args():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("csvw_path", type=Path, help="CSVW file")
    return parser.parse_args()


def main():
    args = get_args()

    with args.csvw_path.open() as file:
        csvw = json.load(file)
        logger.info("Loaded %s", file.name)

        dialect = csvw.get("dialect", dict())

        for table in csvw["tables"]:
            print(table)

            sql = Table(table).to_sql()
            print(sql)


if __name__ == "__main__":
    main()
