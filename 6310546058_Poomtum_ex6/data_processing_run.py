import data_processing as dp

print(dp.cities_data[:10])
print()
print(dp.countries_data[:10])
print()
print(dp.teams_data[:10])
print()
print(dp.players_data[:10])
print()
print(dp.titanic_data[:10])
print()
print(dp.min_max_temp(dp.cities_data))
print()
print(dp.country_list(dp.cities_data))
print()
print(dp.average_country_temp(dp.cities_data))

# your test code for other data_processing functions
# print(dp.country_max_diff_temperature(dp.cities_data))
# print(dp.northern_sounthern_most_cities(dp.cities_data))
# print(dp.population_countries_no_coastline_in_EU(dp.countries_data))
# print(dp.cities_in_EU(dp.cities_data, dp.countries_data))
print(dp.average_EU_city_temperature(dp.cities_data, dp.countries_data))
# print(dp.average_passes(dp.players_data))
# print(dp.max_GF_GA_ratio(dp.teams_data))
# print(dp.whose_player_list(dp.players_data, dp.teams_data))
# print(dp.team_list_passes_per_minute(dp.players_data, dp.teams_data))
# print(dp.twin_list(dp.titanic_data))