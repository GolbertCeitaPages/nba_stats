CREATE TABLE IF NOT EXISTS nba_stats_analytics.compact_team_abbrev AS (
    SELECT team,
           abbreviation,
           MIN(season) AS first_season,
           CASE 
               WHEN MAX(season) = 2025 THEN NULL 
               ELSE MAX(season) 
           END AS last_season,
           SUM(CASE WHEN playoffs = 1 THEN 1 ELSE 0 END) AS made_playoffs
    FROM nba_stats_raw.team_abbrev
    GROUP BY team, abbreviation
    );
    
ALTER TABLE nba_stats_analytics.compact_team_abbrev
ADD CONSTRAINT unique_team_season_abbrev UNIQUE (team, abbreviation, first_season, last_season);

INSERT INTO nba_stats_analytics.compact_team_abbrev (team, abbreviation, first_season, last_season, made_playoffs)
SELECT team, abbreviation, MIN(season) AS first_season,
       CASE WHEN MAX(season) = 2025 THEN NULL ELSE MAX(season) END AS last_season,
       SUM(CASE WHEN playoffs = 1 THEN 1 ELSE 0 END) AS made_playoffs
FROM nba_stats_raw.team_abbrev
GROUP BY team, abbreviation
ON DUPLICATE KEY UPDATE
    made_playoffs = VALUES(made_playoffs), 
    last_season = VALUES(last_season);