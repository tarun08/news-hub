
from app.agent.digest_agent import DigestAgent
from app.scrapper.antropic import AnthropicScraper
from app.scrapper.openai import OpenAiScrapper
from app.scrapper.youtube import YoutubeScrapper  


def run_scraper(hours: int = 24):
    youtube_scraper = YoutubeScrapper()
    openai_scraper = OpenAiScrapper()
    anthropic_scraper = AnthropicScraper()

    openai_articles = openai_scraper.scrap(hours)
    anthropic_articles = anthropic_scraper.scrap(hours)

    if openai_articles:
        article_dicts = [
            {
                "guid": a.guid,
                "title": a.title,
                "url": a.url,
                "published_at": a.published_at, 
                "description": a.description,
                "category": a.category
            }
            for a in openai_articles["articles"]
        ]
    
    
    if anthropic_articles:
        article_dicts = [
            {
                "guid": a.guid,
                "title": a.title,
                "url": a.url,
                "published_at": a.published_at,
                "description": a.description,
                "category": a.category
            }
            for a in anthropic_articles["articles"]
        ]

    
    return {
        "success": bool(openai_articles or anthropic_articles),
        "openai": openai_articles,
        "anthropic": anthropic_articles,
    }

def test_disgest_creation():
    digest_agent = DigestAgent()
    digest_generated = digest_agent.generate_digest(title= "Testing",
                                content='''The design of this reactor was started in the 1980s, as a prototype for a 600 MW FBR. Construction of the first two FBR are planned at Kalpakkam, after a year of successful operation of the PFBR. Other four FBR are planned to follow beyond 2030, at sites to be defined.[20]

                                In 2007, the reactor was planned to begin its operation in 2010, but as of 2019, it was expected to reach first criticality in 2020.[21]

                                In July 2017, it was reported that the reactor is in final preparation to go critical.[22] However in August 2020, it was reported that the reactor might go critical only in December 2021.[23] By February 2021, around ₹6,840 crore (equivalent to ₹77 billion or US$907.84 million in 2023) have been spent in the construction and commissioning of the reactor. The reactor was expected to be operational by October 2022.[3][24]

                                Prime Minister Narendra Modi was in Kalpakkam on 4 March 2024 to witness the initiation of its first core loading. A press release described the PFBR as marking the second stage of India's three-stage nuclear power program.[25]

                                On 31 July 2024, the Atomic Energy Regulatory Board (AERB) approved adding nuclear fuel and starting the chain reaction.[26] But new technical issues crept up, after solving those, the AERB cleared BHAVINI to commence final fuel loading which began on 18 October, 2025. The reactor achieved criticality 6 April 2026.[27][28][29] A few lower power physics experiments will be carried out once sustained nuclear chain reaction is achieved. The next step will link the reactor to electrical grid and start producing power on a commercial basis, pending approval from AERB. Kalpakkam will see the construction of two more fast breeder reactors after the Department of Atomic Energy (DAE) is satisfied with the reactor's performance.[30]

                                Technical details

                                Schematic diagram showing the difference between the loop and pool designs of a liquid metal fast breeder reactor. The pool-type has greater thermal inertia to changes in temperature, which therefore gives more time to shut down/SCRAM during a loss of coolant accident situation.
                                The reactor is a pool type LMFBR with 1,750 tonnes of sodium as coolant. Designed to generate 500 MWe of electrical power, with an operational life of 40 years, it will burn a mixed uranium-plutonium MOX fuel, a mixture of PuO
                                2 and UO
                                2. A fuel burnup of 100 GWd/t is expected. The Fuel Fabrication Facility (FFF), under the direction of Bhabha Atomic Research Centre (BARC), Tarapur is responsible for the fuel rods manufacturing. FFF comes under "Nuclear Recycle Board" of Bhabha Atomic Research Center and has been responsible for fuel rod manufacturing of various types in the past.[citation needed] FFF Tarapur in early 2023 had successfully completed fabrication of 100,000 PFBR fuel elements.[clarification needed][31]

                                Safety considerations
                                The prototype fast breeder reactor has a negative void coefficient, thus ensuring a high level of passive nuclear safety. This means that when the reactor overheats (above the boiling point of sodium) the speed of the fission chain reaction decreases, lowering the power level and the temperature.[32] Similarly, before such a potential positive void condition may form from a complete loss of coolant accident, sufficient coolant flow rates are made possible by the use of conventional pump inertia, alongside multiple inlet-perforations, to prevent the possible accident scenario of a single blockage halting coolant flow.[32]

                                The active-safety reactor decay heat removal system consists of four independent coolant circuits of 8MWt capacity each.[33] Further active defenses against the positive feedback possibility include two independent SCRAM shutdown systems, designed to shut the fission reactions down effectively within a second, with the remaining decay heat then needing to be cooled for a number of hours by the four independent circuits.

                                The fact that the PFBR is cooled by liquid sodium creates additional safety requirements to isolate the coolant from the environment, especially in a loss of coolant accident scenario, since sodium explodes if it comes into contact with water and burns when in contact with air. This latter event occurred in the Monju reactor in Japan in 1995. Another consideration with the use of sodium as a coolant is the absorption of neutrons to generate the radioactive isotope 24
                                Na, which has a 15-hour half life.[34]

                                Commissioning
                                The reactor faced various delays in its commissioning. Initially projected for commissioning in 2010, it faced multiple delays due to technical issues due to first of the kind technology, as informed by Minister of State Shri. Jitendra Singh to the Parliament and a written answer.

                                Core loading began in full swing in October 2025, after the clearance from the AERB.

                                On 6 April 2026, the reactor achieved its first criticality, the initiation of a sustained controlled fission chain reaction.''',
                                article_type="Tech")
    
    print(digest_generated)
