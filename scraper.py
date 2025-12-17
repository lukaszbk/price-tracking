import requests
import json
import os


PORT_IDS = ["7743", "0968", "1480", "4652", "1691", "0585"] 


def fetch_and_save():
    ids_param = ",".join(PORT_IDS)
    
    url = (
        f"https://workplace.vanguard.com/investments/valuationPricesServiceProxy"
        f"?portIds={ids_param}&timePeriodCode=D&priceTypeCodes=MKTP,NAV"
    )
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        print(f"Fetching data for: {ids_param}...")
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        # Check if we have valid content
        if 'fundPrices' in data and 'content' in data['fundPrices']:
            funds = data['fundPrices']['content']
            
            for fund in funds:
                p_id = fund['portId']
                price = fund['price']
                
                # Create the specific filename: e.g., vanguard-7743.txt
                filename = f"prices/vanguard-{p_id}.txt"
                
                # Write the price into the file
                with open(filename, 'w') as f:
                    f.write(str(price))
                
                print(f"Saved {filename}: {price}")
        else:
            print("No fund content found in response.")
            exit(1)

    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    fetch_and_save()
