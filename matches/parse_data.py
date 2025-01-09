import json
import os

def get_file_list(folder_path):
    json_file_list=[]
    try:
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".json"):
                file_path=os.path.join(folder_path,file_name)
                json_file_list.append(file_path)
    except Exception as e:
            print(f"Error: {e}")
    return json_file_list

# def parse_json(json_file_list: list):
#     columns = {
#     "match_no":[], "inning":[], "batting_team":[], "bowling_team":[], 
#     "over":[], "ball":[], "batter":[], "bowler":[], "non_striker":[], 
#     "batsman_runs":[], "extra_runs":[], "total_runs":[], "extras_type":[], 
#     "is_wicket":[], "player_dismissed":[], "dismissal_kind":[], "fielder":[]}
#     for file in json_file_list[:1]:
#         with open(file,'r') as f:
#             data=json.load(f)
#             match_no=data["info"]["event"]["match_number"]
#             columns["match_no"].append(match_no)
#             inning=""
#             batting_team=""
#             bowling_team=""
#             over=""
#             ball=""
#             batter=""
#             bowler=""
#             non_striker=""
#             batsman_runs=""
#             extra_runs=""
#             total_runs=""
#             extras_type=""
#             is_wicket=""
#             player_dismissed=""
#             dismissal_kind=""
#             fielder=""
#             print(match_no)
#             print(data["info"]['teams'])
            
    
            
            

            
            
                
if __name__=="__main__":
    folder_path="./games"
    json_data_list=get_file_list(folder_path)
    parse_json(json_data_list)
    