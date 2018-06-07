SELECT
players.player_name AS player_name
, players.team AS team
, seasons.year AS season
, seasons.conference AS conference
, seasons.coach AS coach
, seasons.win_pcnt AS win_pcnt
, seasons.avg_pts_game AS avg_pts_game
, players.games AS number_of_games_in_season
, players.games_started AS num_games_started
, players.avg_min_per_game AS avg_min_per_game
, players.avg_fg_pcnt AS fg_percent
, players.avg_2pt_pcnt AS _2pt_pcnt
, players.avg_3pt_pcnt AS _3pt_pcnt
, players.avg_ft_pcnt AS ft_pcnt
, players.avg_tr AS avg_rebounds
, players.avg_assists AS avg_assists
, players.avg_steals AS avg_steals
, players.avg_blks AS avg_blocks
, players.avg_pf AS avg_personal_fouls
, players.avg_pts AS avg_points_per_game
FROM
  (SELECT * 
  FROM [seasons.year_v2] 
  WHERE year>='1980'
  ) seasons
    LEFT JOIN
      (SELECT * 
        FROM ([players.UNC_player_stats_1980_1989])
             ,([players.UNC_player_stats_1990_1999] )
             ,([players.UNC_player_stats_2000_2017] )
        )players
      ON seasons.year = players.year
ORDER BY seasons.year DESC



      
