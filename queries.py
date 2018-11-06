from sqlalchemy import create_engine, func, desc, or_
from seed import Company
from statistics import mean
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///dow_jones.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def return_apple():
    return session.query(Company).filter(Company.company == 'Apple').all()[0]

def return_disneys_industry():
    return session.query(Company).filter(Company.company == 'Walt Disney').all()[0].industry

def return_list_of_company_objects_ordered_alphabetically_by_symbol():
    return (session.query(Company).order_by(Company.symbol).all())

def return_list_of_dicts_of_tech_company_names_and_their_EVs_ordered_by_EV_descending():
    tuples = (session.query(Company.company, Company.enterprise_value).order_by(Company.enterprise_value.desc()).all())
    newList = []
    for item in tuples:
        lil_dict = {item[0]: item[1]}
        newList.append(lil_dict)
    return(newList)

def return_list_of_consumer_products_companies_with_EV_above_225():
    return session.query(Company.company).filter(Company.enterprise_value > 225).all()

def return_conglomerates_and_pharmaceutical_companies():
    print(session.query(Company.company, Company.industry).filter(or_(Company.industry == 'Conglomerate', Company.industry == 'Pharmaceuticals')).all())
    # filter(and_(condition1 , condition2))

def avg_EV_of_dow_companies():
    ev_list = session.query(Company.enterprise_value).all()
    ev_list = [ev[0] for ev in ev_list]
    average = mean(ev_list)
    # print(average)
    return average

def return_industry_and_its_total_EV():
    print(session.query(Company.industry, func.sum(Company.enterprise_value)).group_by(Company.industry).order_by((func.sum(Company.enterprise_value)).desc()).all())

# return_apple()
# return_disneys_industry()
# return_list_of_company_objects_ordered_alphabetically_by_symbol()
# return_list_of_dicts_of_tech_company_names_and_their_EVs_ordered_by_EV_descending()
# return_list_of_consumer_products_companies_with_EV_above_225()
# return_conglomerates_and_pharmaceutical_companies()
# avg_EV_of_dow_companies()
return_industry_and_its_total_EV()