drop table if exists nba_stats_analytics.salary_analysis;

create table nba_stats_analytics.salary_analysis as
	select
		shooting.season,shooting.player,
		pos,age,experience,
		shooting.tm,g,mp,
		fg_percent,avg_dist_fga,
		percent_fga_from_x2p_range,
		percent_fga_from_x0_3_range,
		percent_fga_from_x3_10_range,
		percent_fga_from_x10_16_range,
		percent_fga_from_x16_3p_range,
		percent_fga_from_x3p_range,
		fg_percent_from_x2p_range,
		fg_percent_from_x0_3_range,
		fg_percent_from_x3_10_range,
		fg_percent_from_x10_16_range,
		fg_percent_from_x16_3p_range,
		fg_percent_from_x3p_range,
		percent_assisted_x2p_fg,
		percent_assisted_x3p_fg,
		percent_dunks_of_fga,
		num_of_dunks,
		percent_corner_3s_of_3pa,
		corner_3_point_percent,
        ts_percent, per, usg_percent, ows, dws, ws, ws_48, obpm, dbpm, bpm, vorp 
		salary
		from nba_stats_raw.player_shooting as shooting
		left join (
			select * 
            from nba_stats_raw.player_salaries
		) as salary on 
		shooting.player = salary.player and
		shooting.season = salary.season
        left join (
            select player, season, tm, ts_percent, per, usg_percent, ows, dws, ws, ws_48, obpm, dbpm, bpm, vorp 
            from nba_stats_raw.advanced
            where season = 2025
		) as adv on adv.player = shooting.player
		and shooting.tm = adv.tm
		and shooting.season = adv.season
		where shooting.season = '2025'
        and salary is not null
		order by salary desc;