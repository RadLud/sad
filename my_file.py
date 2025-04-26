import pandas as pd

df_poke = pd.read_csv("data/pokemon.csv")

#print (df_poke.shape) #wymiar df


#df_poke_leg = df_poke.groupby('Legendary').sum()

# df_poke_leg = df_poke.sort_values('Attack', ascending=False)


# df_poke_leg = df_poke[df_poke['Legendary'] == True]

# df_poke_leg = df_poke[df_poke['Legendary', 'Attack'] == True]


df_poke_leg = df_poke[['Legendary', 'Defense']].groupby('Legendary').median()

print (df_poke_leg.head(10))
# print (df_poke_leg['Attack'].mean)
