from ..models import State, Chamber, simple_numbered_districts

IA = State(
    name="Iowa",
    abbr="IA",
    capital="Des Moines",
    capital_tz="America/Chicago",
    fips="19",
    unicameral=False,
    legislature_name="Iowa General Assembly",
    division_id="ocd-division/country:us/state:ia",
    jurisdiction_id="ocd-jurisdiction/country:us/state:ia/government",
    url="https://www.legis.iowa.gov/",
    lower=Chamber(
        chamber_type="lower",
        name="House",
        organization_id="ocd-organization/bd11534f-0c3b-4321-8d04-6a42f212bf77",
        num_seats=100,
        title="Representative",
        districts=simple_numbered_districts(
            "ocd-division/country:us/state:ia", "lower", 100
        ),
    ),
    upper=Chamber(
        chamber_type="upper",
        name="Senate",
        organization_id="ocd-organization/a9ad8273-4a86-4544-9bed-09ccb48ebabc",
        num_seats=50,
        title="Senator",
        districts=simple_numbered_districts(
            "ocd-division/country:us/state:ia", "upper", 50
        ),
    ),
)
