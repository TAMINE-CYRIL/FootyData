import pandas as pd
import matplotlib.pyplot as plt

# On ouvre notre dataset sur les clubs
df_club = pd.read_csv("data/clubs.csv")

# Premières statistiques
print("Statistiques concernant la taille des équipes : ")
print(df_club["squad_size"].describe())
print("Statistiques concernant l'âge moyen des équipes : ")
print(df_club["average_age"].describe())



# Moyenne d'étrangers par championnat
df_club.groupby("domestic_competition_id")["foreigners_percentage"].mean().sort_values(ascending=False).plot(kind="bar", title="Valeur"
                                                                                                                       "marchande par championnat")


# Les 10 plus grands stades d'Europe
top_10_stadiums = df_club.sort_values(by="stadium_seats", ascending=False).head(10)
plt.figure(figsize=(12,6))
plt.barh(top_10_stadiums["stadium_name"], top_10_stadiums["stadium_seats"])
plt.title("Les 10 plus grands stades d'Europe")
plt.xlabel("Nombre de places")
plt.ylabel("Nom du stade")
plt.show()

# La distribution de tailles d'effectifs des clubs avec un histogramme
df_club["squad_size"].hist(bins=15)
plt.title("Distribution de tailles d'effectifs des clubs")
plt.xlabel("Nombre de joueurs")
plt.ylabel("Nombre de clubs")
plt.show()

