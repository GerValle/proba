#%% [markdown]
# ### Problema del Cumpleaños
# ---

def proba_cumples(n):
     
    def proba_complemento(n):
        
        if isinstance(n, int):
    
            if n > 1:
                return (365-n +1)/365 * proba_complemento(n-1)
    
            elif n == 1:
                return 365/365
    
            else:
                raise ValueError
            
        else:
            raise TypeError

    return 1-proba_complemento(n)

n = 22
p = proba_cumples(n)

print(f"n: {n} -- proba: {p:.2%}")

# %%
