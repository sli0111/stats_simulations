"""False Positive Report Probability

This script runs simulations for FPRP or the False Positive Report Probability.  
The FPRP is defined as: given a statistically significant result, what is the probability
the null hypothesis is true.

This tool accepts comma separated value files (.csv) as well as excel
(.xls, .xlsx) files.

This script requires that `pandas` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * get_spreadsheet_cols - returns the column headers of the file
    * main - the main function of the script
"""

def calc_fprp(
    comparisons: int = None,
    prior_probability: float = None,
    power: float = 0.8,
    stats_sig_level: float = 0.05
) -> float :
    """Calculates the fprp

    Parameters
    ----------
    comparisons:
        A positive value.  Represents the number of comparison, treatment groups, or experiments being analyzed.
    prior probability:
        A value between 0 and 1 representing our certainty based on our scientific knowledge
        or historical data.  For example, 0.5 means we are 50% certain there will be an effect.
    power:
        A value between 0 and 1.  Represents the probability of detecting an effect if the alternative hypothesis was true.
    stats_sig_level:
        A value between 0 and 1 and commonly written in greek letters as alpha.  
        Used to evaluate whether a p-value from a comparison is statistically significant.

    Returns
    -------
    fprp:
        The FPRP, also commonly called the false positive rate.
    """


    successes = comparisons * prior_probability
    failures = comparisons - successes

    # Number of successes that are stats sig and not stats sig
    stats_sig_success = successes * power

    # Number of failures that are stats sig and not stats sig
    stats_sig_failures = failures * stats_sig_level

    # Calculate fprp
    fprp = stats_sig_failures / (stats_sig_success + stats_sig_failures)

    return fprp


# def calc_prior_probability(
#     comparisons: int = None,
#     fprp: float = None,
#     power: float = 0.8,
#     stats_sig_level: float = 0.05
# ) -> float :
#     """Calculates the fprp

#     Parameters
#     ----------
#     comparisons:
#         A positive value.  Represents the number of comparison, treatment groups, or experiments being analyzed.
#     fprp:
#         The FPRP, also commonly called the false positive rate.
#     power:
#         A value between 0 and 1.  Represents the probability of detecting an effect if the alternative hypothesis was true.
#     stats_sig_level:
#         A value between 0 and 1 and commonly written in greek letters as alpha.  
#         Used to evaluate whether a p-value from a comparison is statistically significant.

#     Returns
#     -------
#     prior_probability:
#         The prior probability we would need to get this false positive rate
#     """


#     successes = comparisons * prior_probability
#     failures = comparisons - successes

#     # Number of successes that are stats sig and not stats sig
#     stats_sig_success = successes * power

#     # Number of failures that are stats sig and not stats sig
#     stats_sig_failures = failures * stats_sig_level

#     # Calculate fprp
#     fprp = stats_sig_failures / (stats_sig_success + stats_sig_failures)

#     return fprp


