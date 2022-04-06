from abc import *
from pandas import DataFrame
from typing import List


class AttrQuery(ABC):
    _index: int
    _name: str
    _select: list = []
    _where: list = []

    def __init__(self, index: int, name: str, attr_dict: dict = None):
        self._index = index
        self._name = name
        if attr_dict is not None:
            self._select = attr_dict['select']
            self._where = attr_dict['where']

    @property
    def name(self) -> str:
        return self._name

    @abstractmethod
    def get_select(self) -> List[str]:
        pass

    @abstractmethod
    def get_where(self) -> List[dict]:
        pass

    @abstractmethod
    def select(self, select: List[str]) -> 'AttrQuery':
        pass

    @abstractmethod
    def where(self, where: List[dict]) -> 'AttrQuery':
        pass


class Attributes(ABC):
    _table_name: str
    _attributes: List[AttrQuery]

    def __init__(self, table_name: str, attributes: List[AttrQuery]):
        self._table_name = table_name
        self._attributes = attributes

    def append(self, attr: AttrQuery):
        self._attributes.append(attr)

    def pop(self):
        self._attributes.pop()

    def all(self) -> List[AttrQuery]:
        return self._attributes

    @property
    def table_name(self) -> str:
        return self._table_name

    @abstractmethod
    def get_by_index(self, idx: int):
        pass

    @abstractmethod
    def get_by_select(self, select: str):
        pass

    @abstractmethod
    def get_by_name(self, name: str):
        pass


class DfQuery(ABC):

    @abstractmethod
    def query(self, query):
        pass

    @abstractmethod
    def build(self):
        pass


class Core(DfQuery):
    _table_name: str
    _df: DataFrame

    @abstractmethod
    def from_dict(self, table_name: str, df_dict: dict, orient: str) -> 'Core':
        pass

    @abstractmethod
    def from_records(self, table_name: str, data_list: List[dict]):
        pass

    @abstractmethod
    def from_df(self, table_name: str, df: DataFrame) -> 'Core':
        pass

    @property
    def df(self) -> DataFrame:
        return self._df

    @abstractmethod
    def table_name(self) -> str:
        pass

    @abstractmethod
    def get_query(self) -> Attributes:
        pass

    @abstractmethod
    def query(self, query_dict: dict) -> 'Core':
        pass