# %%
import requests

# %%
def get_string_net(genes, score=800):
    """Query STRINGdb interactions endpoint"""

    string_api_url = "https://string-db.org/api"
    output_format = "tsv-no-header"
    method = "network"

    request_url = "/".join([string_api_url, output_format, method])

    params = {
        "identifiers": "%0d".join(genes),
        "species": 9606,
        "caller_identity": "www.jvfe.github.io",
        "required_score": score,
    }

    response = requests.post(request_url, data=params)

    return response


# %%
with open("../data/dna_damage.txt", "r") as g:
    genes = g.read().splitlines()

# %%
interactions = get_string_net(genes).text

with open("../results/interactions.tsv", "w") as res:
    res.write(interactions)
