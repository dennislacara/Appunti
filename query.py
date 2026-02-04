
'''
identificare le tuple indipendentemente dall'ordine, da usare nel caso di grafi non orientati

SELECT LEAST(attr1, attr2) AS val_min,
       GREATEST(attr1, attr2) AS val_max,
       COUNT(*) AS occorrenze
FROM coppie
GROUP BY LEAST(attr1, attr2), GREATEST(attr1, attr2);

'''


###Qualche esercizio svolto su ufo
'''
#Nodo: state
#Arco: state1 ↔ state2
#Peso: |avvistamenti(state1) − avvistamenti(state2)|

with tab as(
SELECT s.state , count(*) as avvistamenti
FROM sighting s
GROUP BY s.state
),
tab2 as(
SELECT distinct LEAST(n.state1, n.state2 ) as state1 , GREATEST(n.state1, n.state2) as state2
FROM neighbor n 
),
tab3 as (
SELECT t.state1, t.state2, ABS(ta.avvistamenti - tb.avvistamenti) as peso
from tab2 t
INNER JOIN tab ta on t.state1=ta.state
INNER JOIN tab tb on t.state2 =tb.state
)
SELECT t.state1 , t.state2 , t.peso
FROM tab3 t;


with 
tab as (
	select s.city , s.state , count(*) as avv_relativi
	FROM sighting s 
	GROUP BY s.city , s.state 
),
tab2 as(
	SELECT s.state, count(*) as avv_totali
	FROM sighting s 
	group by s.state 
),
tab3 as(
	SELECT t.city , t.state , t.avv_relativi , ta.avv_totali 
	FROM tab t
	JOIN tab2 ta on t.state = ta.state
)
select *, t.avv_relativi /t.avv_totali *100 as percentuale
from tab3 t
WHERE (t.avv_relativi /t.avv_totali) >= 0.2;


#Nodo: state
#Arco: state A → state B
#Peso: correlazione temporale degli avvistamenti
#	-Due stati sono collegati se:
#		negli stessi anni hanno avuto un incremento >15%
# Peso = numero di anni in comune

WITH tab as(
SELECT s.state , YEAR(s.s_datetime)AS year, count(*) as avv
FROM sighting s 
GROUP BY s.state , YEAR(s.s_datetime)
),
tab2 as(
SELECT ta.state as state1, tb.state as state2, ta.`year` as year1, tb.`year` as year2, ta.avv as avv1, tb.avv as avv2
FROM tab ta, tab tb
WHERE ta.state =tb.state 
	and tb.year = ta.year + 1
),
tab3 as(
SELECT distinct t.state1 , t.year1 , t.year2, (t.avv2 * 1.0 / t.avv1 ) - 1 as percentuale
FROM tab2 t
WHERE (t.avv2 * 1.0 / t.avv1 ) - 1 >= 0.15
),
tab4 as(
SELECT distinct LEAST(ta.state1, tb.state1) as state1, GREATEST(ta.state1, tb.state1) as state2, ta.year1 , tb.year2 
FROM tab3 ta, tab3 tb
where ta.year1 = tb.year1 and ta.year2 = tb.year2 and ta.state1 != tb.state1 
)
SELECT t.state1 , t.state2 , count(*) as incrementi_in_comune
From tab4 t
group by t.state1 , t.state2 

'''


###Qualche esercizio svolto su ufo

'''
#BASEBALL

#               giocatori ~ squadre
#               considerando solo le stagioni in cui il giocatore ha giocato almeno 20 partite.
with tab as(
select a.player_id , a.team_id , sum(a.games)
from appearance a
group by a.player_id, a.team_id, a.`year`
having sum(a.games)>=20
)
select *
from tab ;

#               giocatori ~ giocatori
#               hanno condiviso almeno 2 stagioni nella stessa squadra

with tab_giocatore as (
SELECT s.player_id , s.team_id , s.`year` 
from salary s
),
tab_coppie as(
SELECT distinct ta.player_id player_id1, tb.player_id player_id2, ta.team_id , ta.`year` 
from tab_giocatore ta, tab_giocatore tb
where ta.`year` = tb.`year` and ta.team_id = tb.team_id 
	and ta.player_id  > tb.player_id  
)
select player_id1, player_id2, count(*)
from tab_coppie
group by player_id1, player_id2
having count(*)>=2;




            #Nodo: team
            #Arco: team A → team B
            #Peso: numero di giocatori trasferiti
            
            #Un giocatore crea un arco se:
            #- ha giocato per team A nell’anno Xe per team B nell’anno X+1
            
            #Peso = numero di giocatori che fanno quel passaggio
            
            # (team1, team2, giocatori trasferiti tra due stessi club nello stesso anno)
WITH base AS (
    SELECT
        player_id,
        team_id,
        `year`
    FROM salary
)
SELECT
    b1.team_id AS source,
    b2.team_id AS target,
    COUNT(DISTINCT b1.player_id) AS weight
FROM base b1
JOIN base b2
  ON b1.player_id = b2.player_id
 AND b2.`year` = b1.`year` + 1
WHERE b1.team_id <> b2.team_id
GROUP BY b1.team_id, b2.team_id

'''

###             cromosomi
'''
with tab as(
SELECT distinct g.id, g.cromosoma
FROM gene g 
WHERE g.cromosoma != 0
),
tab2 as (
SELECT distinct i.id_gene1 , i.id_gene2 , i.correlazione
FROM interazione i 
),
tab3 as (
SELECT t2.id_gene1 , t2.id_gene2 , ta.cromosoma as cromosoma1, tb.cromosoma as cromosoma2, t2.correlazione 
FROM tab2 t2 LEFT OUTER JOIN tab ta on t2.id_gene1 = ta.id LEFT OUTER JOIN tab tb on t2.id_gene2 = tb.id
Where ta.cromosoma IS NOT NULL AND tb.cromosoma IS NOT NULL and ta.cromosoma != tb.cromosoma 
),
tab4 as(
SELECT distinct t.cromosoma1 , t.cromosoma2 , correlazione
FROM tab3 t
)
select t.cromosoma1, t.cromosoma2, SUM(t.correlazione)
from tab4 t
group by t.cromosoma1 , t.cromosoma2

'''