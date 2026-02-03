
'''
identificare le tuple indipendentemente dall'ordine, da usare nel caso di grafi non orientati

SELECT LEAST(attr1, attr2) AS val_min,
       GREATEST(attr1, attr2) AS val_max,
       COUNT(*) AS occorrenze
FROM coppie
GROUP BY LEAST(attr1, attr2), GREATEST(attr1, attr2);

'''