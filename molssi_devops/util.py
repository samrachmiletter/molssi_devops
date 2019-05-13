"""
util.py
A file containing utility functions.
"""

def title_case(sentence):
    """
    Convert a string into title case.
    Title case means that the first letter of each word is capitalized with all other letters lower case.

    Parameters
    ----------
    sentence : string
        String to be converted into title case.

    Returns
    -------
    title : string
        String in title case format.

    Example
    -------
    >>>title_case("ThiS iS a StriNg tO be conVerTed")
    'This Is A String To Be Converted'
    """

    if not isinstance(sentence, str):
        raise TypeError('Invalid, type %s - Input must be type string' % (type(sentence)))


    words = sentence.split()
    title = ""
    for word in words:
        title += word[0].upper() + word[1:].lower() + " "
    return title

