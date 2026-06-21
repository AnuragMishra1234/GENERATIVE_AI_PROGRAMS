#!pip install langchain langchain-community langchain-google-genai
#!pip install wikipedia pydanticimport wikipedia
#!pip install -U wikipedia
#!pip install -U langchain-community wikipedia-api
from pydantic import BaseModel
from typing import Optional

class InstitutionInfo(BaseModel):
    name: str
    founder: Optional[str] = None
    founded_year: Optional[str] = None
    branches: Optional[str] = None
    employees: Optional[str] = None
    summary: Optional[str] = None

class InstitutionParser:

    @staticmethod
    def parse_wikipedia_summary(institution_name: str) -> Optional[InstitutionInfo]:

        try:
            # Search for institution
            results = wikipedia.search(institution_name, results=3)

            if not results:
                print("No matching institution found on Wikipedia.")
                return None

            # Best match
            best_match = results[0]

            # Get summary
            summary = wikipedia.summary(best_match, sentences=5)

            # Try to get page content
            try:
                page = wikipedia.page(best_match)
                content = page.content.lower()
            except:
                content = ""

            founder = InstitutionParser.extract_info(
                content,
                ["founder", "founded by"]
            )

            founded_year = InstitutionParser.extract_info(
                content,
                ["founded", "established"]
            )

            branches = InstitutionParser.extract_info(
                content,
                ["branches", "campuses", "locations"]
            )

            employees = InstitutionParser.extract_info(
                content,
                ["employees", "staff", "faculty"]
            )

            return InstitutionInfo(
                name=best_match,
                founder=founder,
                founded_year=founded_year,
                branches=branches,
                employees=employees,
                summary=summary
            )

        except Exception as e:
            print(f"Error fetching details: {e}")
            return None

    @staticmethod
    def extract_info(content: str, keywords: list) -> Optional[str]:

        for keyword in keywords:

            index = content.find(keyword)

            if index != -1:
                snippet = content[index:index + 120]
                return snippet.split(".")[0].strip()

        return None

institution_name = input("Enter Institution Name: ")

institution_details = InstitutionParser.parse_wikipedia_summary(
    institution_name
)

if institution_details:

    print("\n" + "=" * 50)
    print("INSTITUTION DETAILS")
    print("=" * 50)

    print(f"Institution Name : {institution_details.name}")

    print(
        f"Founder          : {institution_details.founder if institution_details.founder else 'Not Available'}"
    )

    print(
        f"Founded Year     : {institution_details.founded_year if institution_details.founded_year else 'Not Available'}"
    )

    print(
        f"Branches         : {institution_details.branches if institution_details.branches else 'Not Available'}"
    )

    print(
        f"Employees        : {institution_details.employees if institution_details.employees else 'Not Available'}"
    )

    print("\nSUMMARY")
    print("-" * 50)
    print(
        institution_details.summary
        if institution_details.summary
        else "Not Available"
    )

else:
    print("Institution details could not be retrieved.")