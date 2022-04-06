# DfQuery

Pandas DataFrame 조회를 양식화된 JSON(내부에선 딕셔너리 객체)으로 원하는 값을 가져올 수 있습니다.

## 목적

## 사용법

### install

```
git clone https://github.com/miniyus/dfquery
cd dfquery
python setup.py install
```

### 기본 예시

```python
import dfquery
import json

# single table
file = open('table_file_path')
json_dict = json.load(file)
query = dfquery.make('table_name', json_dict)

query_dict = json.load(open('query_file_path'))
query.query(query_dict)
print(query.build())

# multiple table
file = open('table_file_path')
json_dict = json.load(file)
query = dfquery.batch(json_dict)

query_dict = json.load(open('query_file_path'))
query.query(query_dict)
print(query.build())
```

### dfquery.make()

```python
import pandas
import dfquery

"""
데이터 프레임으로 변환 가능한 객체
"""
data = pandas.DataFrame()
dfquery.make('table_name', data)

"""
딕셔너리의 경우, 데이터 프레임의 from_dict 메서드를 사용하기 때문에
orient 파라미터가 존재합니다. 딕셔너리 구조에 맞게 사용하세요.
"""
data = {}
dfquery.make('table_name', data)

"""
list[dict] 형태의 records 형식은 from_records 메서드를 사용하여 dataframe으로 변환합니다.
"""
data = [{}]
dfquery.make('table_name', data)

```

### dfquery.batch()

```python
import dfquery

"""
make에서 사용된 구조와 동일한 형식의 데이터들이 딕셔너리로 감싸진 형태

{
  "table_1" : data(Type: DataFrame, list[dict], dict),
  "table_2" : data(Type: DataFrame, list[dict], dict)
}

딕셔너리의 경우 make와 동일하게 orient 파라미터가 존재하지만, 모든 테이블이 같은 구조일경우만 정상 작동합니다.
"""
batch_data = {}
query = dfquery.batch({
    "table_1": [{...}],
    "table_2": [{...}]
})

```

### 쿼리 구조

```json
{
  "table_name": {
    "name(결과를 찾을 때 사용)": {
      "select": [
        "column_name"
      ],
      "where": [
        {
          "key": "column_name",
          "operator": "파이썬 비교 연산자",
          "value": "find_value"
        }
      ]
    },
    "name2": {
      "select": [
        "column_name"
      ],
      "where": [
        {
          "key": "column_name",
          "operator": "파이썬 비교 연산자",
          "value": "find_value"
        }
      ]
    }
  }
}
```

**문법**

- select: 가져올 컬럼명 리스트
- where:
    - key: 조건에 사용할 컬럼명
        - operator: 비교 조건, python에서 사용하는 기본 비교 연산자 사용 가능
            - *like: 와일드카드```"*"```를 사용(SQL like와 유사하다.)
                - ```"*ABC*"```: ABC가 포함된 값 찾기
                - ```"*ABC"```: ABC(으)로 끝나는 값 찾기
                - ```"ABC*"```: ABC(으)로 시작하는 값 찾기
          ```json
          {
            "operator": "like",
            "value": "*ABCV*"    
          }
          ```
    - where절도 리스트이기 때문에 여러개의 조건을 포함할 수 있으나 OR 조건처럼 작동한다.
