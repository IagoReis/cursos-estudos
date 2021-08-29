**took**: quanto tempo em milissegundos levou a consulta.

**timed_out**: boolean informado que a consulta foi abortada por time out, tempo de consulta excedido.

**_shards**: objeto de shard
    - **total**: quantidade total de shards afetadas com a consulta
    - **successful**: quantidade de shards que retornaram dados com sucesso
    - **failed**: quantidade de shards que falharam

**hits**: objeto hitis contem a informação dos dados retornados
    - **total**: quantos registros foram encontrados
    - **max_score**: valor entre 0 e 1, relevância ou valor de semelhança
    - ****: