from scipy.stats import chi2_contingency

def find_chi2_independence(cat_attr, target, data, alpha=0.05):
       
    print(f"---------------{target} Vs {cat_attr} Chi Square Test of Independence -------------------")
    print(f"Null Hypothesis: {target} and {cat_attr} has no relationship")
    print(f"Alternate Hypothesis : {cat_attr} and {cat_attr} has significant relationship")

#     print(f"\n Contingency table :\n")
#     print(tab)
    observed_values = pd.crosstab(data[target],data[cat_attr]).values
    stat, p, dof, expected = chi2_contingency(observed_values)
#     print(p)
#     print(f"\n Expected table :\n")
#     print(expected)
    
#     print(f"The p value returned = {p} and degrees of freedom returned = {dof}")
    
    # interpret p-value
    print('significance(alpha) = %.3f' % (alpha))

    if p <= alpha:
        print('Dependent (reject H0)')
    else:
        print('Independent (Accept Null Hypothesis H0)') 