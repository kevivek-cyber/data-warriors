import dash
from dash import dcc, html, Input, Output, State, ALL
import pandas as pd
import os
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import dash_table 
import spacy
import re

# nlp = spacy.load("en_core_web_sm")


# def extract_details(text):
#     doc = nlp(text)

   
#     name = ""
#     for ent in doc.ents:
#         if ent.label_ == "PERSON":
#             name = ent.text
#             break

   
#     if not name:
#         lines = text.strip().split("\n")
#         if lines:
#             name = lines[0]
            
#     skill_keywords = [
#         'python','java','cpp','c','javascript','typescript','react',
#         'angular','vue','nodejs','django','flask','sql','pandas',
#         'numpy','machine learning','data science','docker','aws','git'
#     ]



app = dash.Dash(__name__)

file_path = "users.csv"
admin_path = "admin.csv"


def quiz_pie_chart(score):
    fig = go.Figure(go.Pie(
        values=[score, 3-score],  # score vs remaining
        labels=['Scored', 'Remaining'],
        hole=0.6,
        marker_colors=['#00cc96', '#e9ecef'],
        textinfo='none'
    ))

    

if not os.path.exists(file_path):
    pd.DataFrame(columns=['Name','Passing Year','Aquired Skill','Enter Collage','Year of Experience','Quiz Score','Score','Projects']).to_csv(file_path, index=False)

if not os.path.exists(admin_path):
    pd.DataFrame(columns=['Required Skills']).to_csv(admin_path,index=False)
    
def admin_file(give_list):
    
    admin_df = pd.DataFrame({'Required Skills':[give_list]})
    admin_df.to_csv(admin_path, index=False)
    
show_df = pd.read_csv("users.csv")
soham_df3 = pd.read_csv('admin.csv')

show_df['Year of Experience'] = pd.to_numeric(show_df['Year of Experience'], errors='coerce').fillna(0)
show_df['Quiz Score'] = pd.to_numeric(show_df['Quiz Score'], errors='coerce').fillna(0)
show_df['Year of Experience'] = show_df['Year of Experience'].sort_values(ascending=True)
show_df['matches'] = show_df['Aquired Skill'].apply(
    lambda x: int(any(skill in soham_df3['required_skills'].values for skill in x))
)
show_df['Performance'] = pd.to_numeric(show_df['matches'], errors='coerce') + pd.to_numeric(show_df['Quiz Score'], errors='coerce') + pd.to_numeric(show_df['Year of Experience'], errors='coerce')
fig = px.bar(show_df,x="Name",y='Performance',title="Candidate Dash")
print(show_df)





show_df.columns = show_df.columns.str.strip()


show_df['Name'] = show_df['Name'].str.strip()




jobs_skills = {
    "Software Developer": [
        "python", "java", "cpp", "c", "git",
        "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy"
    ],
    
    "Web Developer": [
        "html", "css", "javascript", "typescript",
        "react", "angular", "vue", "nodejs", "git",
        "dummy", "dummy", "dummy", "dummy"
    ],
    
    "Backend Developer": [
        "python", "java", "nodejs", "django", "flask",
        "sql", "git",
        "dummy", "dummy", "dummy", "dummy", "dummy", "dummy"
    ],
    
    "Frontend Developer": [
        "html", "css", "javascript", "typescript",
        "react", "angular", "vue", "git",
        "dummy", "dummy", "dummy", "dummy", "dummy"
    ],
    
    "Full Stack Developer": [
        "html", "css", "javascript", "typescript",
        "react", "angular", "nodejs",
        "python", "django", "flask",
        "sql", "git", "dummy"
    ],
    
    "Mobile App Developer": [
        "kotlin", "swift", "javascript", "react",
        "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy"
    ],
    
    "Data Analyst": [
        "python", "sql", "pandas", "numpy",
        "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy"
    ],
    
    "Data Scientist": [
        "python", "machine_learning", "data_science",
        "pandas", "numpy", "sql",
        "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy"
    ],
    
    "Machine Learning Engineer": [
        "python", "machine_learning", "pandas",
        "numpy", "docker", "aws",
        "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy"
    ],
    
    "DevOps Engineer": [
        "docker", "aws", "git", "python",
        "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy"
    ],
    
    "Cloud Engineer": [
        "aws", "docker", "python", "git",
        "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy"
    ],
    
    "Cybersecurity Analyst": [
        "python", "c", "cpp", "git",
        "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy"
    ],
    
    "Game Developer": [
        "cpp", "c", "python",
        "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy"
    ],
    
    "Embedded Systems Engineer": [
        "c", "cpp",
        "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy"
    ],
    
    "Scripting Engineer / Automation Engineer": [
        "python", "git",
        "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy"
    ]
}


df_for_job = pd.DataFrame(jobs_skills)
show_table = pd.DataFrame(columns=['Job Matches','Aquired Skill','Required Skill'])








value3=['python']
columns_with_python = df_for_job.isin(value3).sum(axis=0)






result_value = columns_with_python[columns_with_python==columns_with_python.max()].index.tolist()


final_value=[result_value][0]
array = np.array(final_value)

show_table['Job Matches']=array
show_table['Aquired Skill']=value3+value3*(len(show_table['Job Matches'])-1)

show_table['list']=show_table['Job Matches'].apply(lambda x : df_for_job[x].tolist())
show_table['new_col_soham']=show_table['list'].apply(lambda list : [x for x in list if x != "dummy"])


show_table['Required Skill']=show_table['new_col_soham'].apply(lambda x : ','.join(x))














    

questions = [
    {
        "id": "q1",
        "question": "NumPy: What does np.array() do?",
        "options": ["Creates list", "Creates array", "Sorts data"],
        "answer": "Creates array"
    },
    {
        "id": "q2",
        "question": "Pandas: What is a DataFrame?",
        "options": ["1D array", "2D tabular structure", "Graph"],
        "answer": "2D tabular structure"
    },
    {
        "id": "q3",
        "question": "Dash: What is it used for?",
        "options": ["Game dev", "Web dashboards", "Database"],
        "answer": "Web dashboards"
    }
]

def generate_questions():
    return [
        html.Div([
            html.P(q["question"]),
            dcc.RadioItems(
                id={"type": "question", "index": q["id"]},
                options=[{"label": opt, "value": opt} for opt in q["options"]],
            )
        ]) for q in questions
    ]
    


fig.update_layout(
    paper_bgcolor="#daab72",  # transparent figure background '#686a2a
    plot_bgcolor="#e6e9be"    # transparent plot area
    
)



app.layout = html.Div([
    
    html.Div([
        dcc.Store(id="candidate_data", data={}),
        dcc.Store(id="quiz-store", data={}),
        html.H2("Welcome to our Prototype",
            style={'color':'black','margin':'0px','padding':'0px','textAlign':'center','size':'3px'}),
        
    ],
    style={'background-color':'#707F62','height':"43px",'display':'flex','textAlign':'center','justifyContent':'center','alignItems':'center','borderRadius':'8px'}),

    html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Button(
                "Upload Resume",
                style={'backgroundColor':'transparent','color':"#A55EE3",'border':'2px solid #A55EE3','padding':'9px 11px','fontSize':'16px','borderRadius':'8px','cursor':'pointer'}
            )
        ),

        html.Div([
            html.H2("Or", style={'margin':'0px','padding':'0px'}),

            dcc.Input(placeholder="Enter Name", id='name', style={'width':'293px'}),
            dcc.Input(placeholder="Passing Year", id='year', style={'width':'293px'}),

            dcc.Dropdown(
                placeholder="Aquired Skill",
                id='skills',
                multi=True,
                options=[
                    {'label': 'Python', 'value': 'python'},
                    {'label': 'Java', 'value': 'java'},
                    {'label': 'C++', 'value': 'cpp'},
                    {'label': 'C', 'value': 'c'},
                    {'label': 'JavaScript', 'value': 'javascript'},
                    {'label': 'TypeScript', 'value': 'typescript'},
                    {'label': 'Go', 'value': 'go'},
                    {'label': 'Rust', 'value': 'rust'},
                    {'label': 'Kotlin', 'value': 'kotlin'},
                    {'label': 'Swift', 'value': 'swift'},
                    {'label': 'PHP', 'value': 'php'},
                    {'label': 'Ruby', 'value': 'ruby'},
                    {'label': 'HTML', 'value': 'html'},
                    {'label': 'CSS', 'value': 'css'},
                    {'label': 'React', 'value': 'react'},
                    {'label': 'Angular', 'value': 'angular'},
                    {'label': 'Vue.js', 'value': 'vue'},
                    {'label': 'Node.js', 'value': 'nodejs'},
                    {'label': 'Django', 'value': 'django'},
                    {'label': 'Flask', 'value': 'flask'},
                    {'label': 'Machine Learning', 'value': 'machine_learning'},
                    {'label': 'Data Science', 'value': 'data_science'},
                    {'label': 'Pandas', 'value': 'pandas'},
                    {'label': 'NumPy', 'value': 'numpy'},
                    {'label': 'SQL', 'value': 'sql'},
                    {'label': 'Docker', 'value': 'docker'},
                    {'label': 'AWS', 'value': 'aws'},
                    {'label': 'Git', 'value': 'git'}
                ],
                style={'width':'293px'}
            ),

            dcc.Input(placeholder="Enter Collage", id='collage', style={'width':'293px'}),
            dcc.Input(placeholder="Year of Experience", id='exp', style={'width':'293px'}),

            dcc.Button("Confirm & attempt Quiz", id="fill_form", n_clicks=0, style={'margin':'13px 13px'}),

            html.Div(id='op', style={'color':'#686a2a'}),
            dcc.Store(id="for_admin")
        ],
        style={'color':'#686a2a','display':'flex','flexDirection':'column','alignItems':'center','margin':'0px','padding':'9px 11px'})
    ],
    style={'margin-top':'3px','background-color':'#c1bd96','display':'flex','textAlign':'center','justifyContent':'center','alignItems':'center','borderRadius':'8px','gap':'93px'}),
    html.Div(id='job_matches_div'),
    
    html.Div(
        id="quiz-container",
        style={'display':'none','flexDirection':'column','gap':'20px','background-color':'#B7D69F','borderRadius':'13px','padding':'20px'},
        children=[
            html.H2("Quiz Based on skills"),
            *generate_questions(),
            html.Button("Submit Quiz", id="submit-quiz"),
            html.Div(id="quiz-result")
        ]
    ),
    html.Div([
        html.H2("Admin Section",style={'color':'#D5D55C',
                                       'margin_top':'1px',
        'padding':'0px'}),
        dcc.Dropdown(
                placeholder="Required Skill",
                id='skills_req',
                multi=True,
                options=[
                    {'label': 'Python', 'value': 'python'},
                    {'label': 'Java', 'value': 'java'},
                    {'label': 'C++', 'value': 'cpp'},
                    {'label': 'C', 'value': 'c'},
                    {'label': 'JavaScript', 'value': 'javascript'},
                    {'label': 'TypeScript', 'value': 'typescript'},
                    {'label': 'Go', 'value': 'go'},
                    {'label': 'Rust', 'value': 'rust'},
                    {'label': 'Kotlin', 'value': 'kotlin'},
                    {'label': 'Swift', 'value': 'swift'},
                    {'label': 'PHP', 'value': 'php'},
                    {'label': 'Ruby', 'value': 'ruby'},
                    {'label': 'HTML', 'value': 'html'},
                    {'label': 'CSS', 'value': 'css'},
                    {'label': 'React', 'value': 'react'},
                    {'label': 'Angular', 'value': 'angular'},
                    {'label': 'Vue.js', 'value': 'vue'},
                    {'label': 'Node.js', 'value': 'nodejs'},
                    {'label': 'Django', 'value': 'django'},
                    {'label': 'Flask', 'value': 'flask'},
                    {'label': 'Machine Learning', 'value': 'machine_learning'},
                    {'label': 'Data Science', 'value': 'data_science'},
                    {'label': 'Pandas', 'value': 'pandas'},
                    {'label': 'NumPy', 'value': 'numpy'},
                    {'label': 'SQL', 'value': 'sql'},
                    {'label': 'Docker', 'value': 'docker'},
                    {'label': 'AWS', 'value': 'aws'},
                    {'label': 'Git', 'value': 'git'}
                ],
                style={'width':'293px'}
            ),
        dcc.Button(
            "Confirm",
            id="admin_btn",
            n_clicks=0,
            style={
                'color':'#D5D55C',
                'background-color': '#686a2a'
            }
        ),
        html.Div(id='updated_graph'),
        
        dcc.Dropdown(
            
            placeholder="Name",
            id="name_info",
            options=[{'label':k,'value':k}for k in show_df['Name']]
        ),
        # html.Div([
        #     html.H2("Data Table"),
        #     dash_table.DataTable(
                
                
        #         data=show_table.to_dict('records'),
        #         columns=[{'name':col,'id':col} for col in show_table.columns]
                
                
                
                
        #     )
            
        # ]),
        
        
                        
        
        
        
        html.Div([
            
            
            html.P("This dashboard is for prototype Purpose Only",
                   
                   style={'color':'white'}),
            html.P("Due to lack of Cloud Storage Instant Changes will not be Reflected",
                   
                   style={'color':'white'})
        ]),
        
        
        
        
        
        
        
        
    ],style={
        'display':'flex',
        'gap':'13px',
        'margin_top':'3px',
        'padding':'0px',
        'alignItems':'center',
        'justifyContent':'center',
        'background-color':'#707F62',
        'flexDirection':'column'
        
    }),
    html.Div(id="complete_detail3"),
    html.Div(id="complete_detail"),

    
])



@app.callback(
    Output('complete_detail','children'),
    Output('complete_detail3','children'),
    Input('name_info','value'),
)
def info(index):
    if not index:
        return html.Div("Select a candidate to see details"),dash.no_update

    candidate = show_df[show_df['Name'] == index].iloc[0]

    score = candidate['Quiz Score']
    total = 3

    fig3 = px.pie(
        names=['Scored', 'Remaining'],
        values=[score, total - score],
        hole=0.4,
        title=f"{candidate['Name']}'s Quiz Score out of 3"
    )
    fig3.update_layout(
        paper_bgcolor="#e6e9be",  
        plot_bgcolor="#e6e9be"    
        
    )

    return html.Div([
        html.H3("                                "),
        html.P(f"Passing Year: {candidate['Passing Year']}"),
        html.P(f"Acquired Skill: {candidate['Aquired Skill']}"),
        html.P(f"Collage: {candidate['Enter Collage']}"),
        html.P(f"Year of Experience: {candidate['Year of Experience']}"),
        html.P(f"Quiz Score: {candidate['Quiz Score']} / 3"),
        dcc.Graph(figure=fig3)
    ],style={'display':'flex',
             'justifyContent':'center',
             'alignItems':'center',
             'gap':'13px',
             'background-color':"#e6e9be",
             'margin':'0px',
             'padding':'0px',
             
             
             }),html.Div([
                html.H3(f"Candidate: {candidate['Name']}"),
                 
             ],style={'display':'flex',
                       'justifyContent':'center',
                        'alignItems':'center',
                        'background-color':"#e6e9be",
                        
                      
                      })
                   
    
    #     html.H4(row['Name']),
    #     html.P(f"Passing Year: {row['Passing Year']}"),
    #     html.P(f"Acquired Skill: {row['Acquired Skill']}"),
    #     dcc.Graph(figure=quiz_pie_chart(row['Quiz Score'])),
    #     html.P(f"Performance: {row['Performance']}")
    # ], style={
    #     'border': '1px solid #ccc',
    #     'padding': '15px',
    #     'margin': '10px',
    #     'borderRadius': '10px',
    #     'width': '200px',
    #     'display': 'inline-block',
    #     'textAlign': 'center',
    #     'boxShadow': '2px 2px 5px #aaa'
    # })
    

@app.callback(
    Output('job_matches_div','children'),
    Input('skills','value'),
    Input('fill_form','n_clicks')
)
def show_matches(value3,n):
    if n and value3:
        columns_with_python = df_for_job.isin(value3).sum(axis=0)
        result_value = columns_with_python[columns_with_python==columns_with_python.max()].index.tolist()
        
        final_value=[result_value][0]
   
        show_table = pd.DataFrame({'Job Matches': result_value})
        
        show_table['Aquired Skill'] = [', '.join(value3)] * len(show_table)
        
        show_table['list']=show_table['Job Matches'].apply(lambda x : df_for_job[x].tolist())
        show_table['new_col_soham']=show_table['list'].apply(lambda list : [x for x in list if x != "dummy"])


        show_table['Required Skill']=show_table['new_col_soham'].apply(lambda x : ','.join(x))
        # print(show_table.to_html)
        return html.Div([ 
                         
                         
                        #  "hi soham bharat zaware",
                        #  html.H3("Data Table"),
                         dash_table.DataTable(
    data=show_table[['Job Matches','Aquired Skill','Required Skill']].to_dict('records'),
    columns=[
        {'name': 'Job Matches', 'id': 'Job Matches'},
        {'name': 'Aquired Skill', 'id': 'Aquired Skill'},
        {'name': 'Required Skill', 'id': 'Required Skill'}
    ],

    style_table={
        'overflowX': 'auto',
        'borderRadius': '12px',
        'boxShadow': '0px 4px 15px rgba(0,0,0,0.3)'
    },

    style_header={
        'backgroundColor': 'rgb(213, 213, 92)',
        'color': '#000',
        'fontWeight': 'bold',
        'fontSize': '16px',
        'textAlign': 'center',
        'border': 'none'
    },

    style_cell={
        'backgroundColor': '#2c2c2c',
        'color': 'white',
        'textAlign': 'left',
        'padding': '12px',
        'fontFamily': 'Segoe UI',
        'border': 'none'
    },

    style_data={
        'borderBottom': '1px solid #444'
    },

    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': '#252525'
        },
        {
            'if': {'column_id': 'Job Matches'},
            'color': 'rgb(213, 213, 92)',
            'fontWeight': 'bold'
        }
    ],

    page_size=5
)
                        
                        # show_table.to_dict('index')
                             
                         
                         
       
])

@app.callback(
    Output('updated_graph','children'),
    Output('skills_req','value'),
    Input('admin_btn','n_clicks'),
    State('skills_req','value')
)
def admin_confirm(n,value):
    if not n or not value:
        return dash.no_update
    global soham_df
    show_df = pd.read_csv("users.csv")
    soham_df3 = pd.read_csv('admin.csv')
    
    print("-----------------checking how value looks ------------------->")
    print(value)
    newval=(",".join(value))
    print("---------------------------------------------------------------->")
    print("---------------Value look in column------------------------>")
    
    soham_df = pd.DataFrame({'required_skills':[newval]})
    print(soham_df)
    print(soham_df['required_skills'])
    print("-------------------Cheking how i can add col by trans--------------->")
    show_df['try_333']=soham_df['required_skills']

    val=soham_df.loc[0,'required_skills']
    show_df['try_333']=show_df['try_333'].fillna(val)

    print("-----------------Cheking the matches ---------3------------------>")
    
    show_df['new_matches']=np.sum(show_df['Aquired Skill'].any()==show_df['try_333'].any())
    print(show_df.loc[[i for i in range(len(show_df['Aquired Skill']))],'Aquired Skill'].to_string())
    print(show_df['Aquired Skill'].astype('string'))
    # print(soham_df.loc[[i for i in range(len(soham_df['required_skills']))],'required_skills'][0])
    print("---------------------------set logic ---------------------------->")

    show_df['Aquired Skill_set'] = show_df['Aquired Skill'].apply(lambda x: set(i.strip() for i in x.split(',')))
    show_df['try_333_set'] = show_df['try_333'].apply(lambda x: set(i.strip() for i in x.split(',')))

   
    show_df['new_matches'] = show_df.apply(lambda x: x['try_333_set'].issubset(x['Aquired Skill_set']), axis=1)
    print("---------------------------new_matches _____________>")
    show_df['new_matches'] = show_df.apply(lambda x: len(x['Aquired Skill_set'] & x['try_333_set']), axis=1)
    print(show_df[['Aquired Skill', 'try_333', 'new_matches']])




    print("---------------------------------------------------------------->")
    
    soham_df.to_csv("admin.csv",index=False)
    
    
    
    
    
    
    show_df['Year of Experience'] = pd.to_numeric(show_df['Year of Experience'], errors='coerce').fillna(0)
    show_df['Quiz Score'] = pd.to_numeric(show_df['Quiz Score'], errors='coerce').fillna(0)
    show_df['Year of Experience'] = show_df['Year of Experience'].sort_values(ascending=True)
    show_df['matches'] = show_df['Aquired Skill'].apply(
        lambda x: int(any(skill in soham_df3['required_skills'].values for skill in x))
    )
    print(show_df['matches'])
    print(soham_df)
    print("--------------------------------------->")
    print(soham_df3['required_skills'])
    print(show_df['Aquired Skill'])
    
    
    
    # show_df['new3']=soham_df3['required_skills'].transform()
    print("-----------------------------------trying----------------------->")
    print(show_df)
    
    
    
    show_df['Performance'] = pd.to_numeric(show_df['new_matches'], errors='coerce') + pd.to_numeric(show_df['Quiz Score'], errors='coerce') + pd.to_numeric(show_df['Year of Experience'], errors='coerce')
    fig = px.bar(show_df,x="Name",y='Performance',title="Candidate Dash")
    
    return dcc.Graph(
        figure=fig,
        
        
    ), dash.no_update  
    
    
    
    
    
    



@app.callback(
    Output('op','children'),
    Output('candidate_data','data'),
    Output('quiz-container','style'),
    Input('fill_form','n_clicks'),
    State('name','value'),
    State('year','value'),
    State('skills','value'),
    State('collage','value'),
    State('exp','value'),
)
def show(n, name, year, skills, collage, exp):
    if n:
        if not name or not year or not skills or not collage or not exp:
            return "Please enter all the values", {}, {'display':'none'}
        
        show_df = pd.read_csv("users.csv")
        soham_df3 = pd.read_csv('admin.csv')
        
        
        
        show_df['Year of Experience'] = pd.to_numeric(show_df['Year of Experience'], errors='coerce').fillna(0)
        show_df['Quiz Score'] = pd.to_numeric(show_df['Quiz Score'], errors='coerce').fillna(0)
        show_df['Year of Experience'] = show_df['Year of Experience'].sort_values(ascending=True)
        show_df['matches'] = show_df['Aquired Skill'].apply(
            lambda x: int(any(skill in soham_df3['required_skills'].values for skill in x))
        )
        show_df['Performance'] = pd.to_numeric(show_df['matches'], errors='coerce') + pd.to_numeric(show_df['Quiz Score'], errors='coerce') + pd.to_numeric(show_df['Year of Experience'], errors='coerce')
        fig = px.bar(show_df,x="Name",y='Performance',title="Candidate Dash")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        data = {
            'Name': name,
            'Passing Year': year,
            'Aquired Skill': skills,
            'Enter Collage': collage,
            'Year of Experience': exp
        }

        return "Proceed to quiz", data, {'display':'flex','flexDirection':'column','gap':'20px','background-color':'#B7D69F','padding':'20px'}

    return "", {}, {'display':'none'}

@app.callback(
    Output("quiz-store", "data"),
    Input({"type": "question", "index": ALL}, "value"),
)
def store_answers(values):
    show_df = pd.read_csv("users.csv")
    soham_df3 = pd.read_csv('admin.csv')
    
    
    
    show_df['Year of Experience'] = pd.to_numeric(show_df['Year of Experience'], errors='coerce').fillna(0)
    show_df['Quiz Score'] = pd.to_numeric(show_df['Quiz Score'], errors='coerce').fillna(0)
    show_df['Year of Experience'] = show_df['Year of Experience'].sort_values(ascending=True)
    show_df['matches'] = show_df['Aquired Skill'].apply(
        lambda x: int(any(skill in soham_df3['required_skills'].values for skill in x))
    )
    show_df['Performance'] = pd.to_numeric(show_df['matches'], errors='coerce') + pd.to_numeric(show_df['Quiz Score'], errors='coerce') + pd.to_numeric(show_df['Year of Experience'], errors='coerce')
    fig = px.bar(show_df,x="Name",y='Performance',title="Candidate Dash")
    
    
    
    data = {}
    for i, v in enumerate(values):
        data[questions[i]["id"]] = v
    return data

def calculate_score(data):
    score = 0
    show_df = pd.read_csv("users.csv")
    soham_df3 = pd.read_csv('admin.csv')
    
    
        
    show_df['Year of Experience'] = pd.to_numeric(show_df['Year of Experience'], errors='coerce').fillna(0)
    show_df['Quiz Score'] = pd.to_numeric(show_df['Quiz Score'], errors='coerce').fillna(0)
    show_df['Year of Experience'] = show_df['Year of Experience'].sort_values(ascending=True)
    show_df['matches'] = show_df['Aquired Skill'].apply(
        lambda x: int(any(skill in soham_df3['required_skills'].values for skill in x))
    )
    show_df['Performance'] = pd.to_numeric(show_df['matches'], errors='coerce') + pd.to_numeric(show_df['Quiz Score'], errors='coerce') + pd.to_numeric(show_df['Year of Experience'], errors='coerce')
    fig = px.bar(show_df,x="Name",y='Performance',title="Candidate Dash")
    
    
    
    for q in questions:
        if data.get(q["id"]) == q["answer"]:
            score += 1
    return score

@app.callback(
    Output("quiz-result", "children"),
    Input("submit-quiz", "n_clicks"),
    State("quiz-store", "data"),
    State("candidate_data", "data")
)
def submit_quiz(n, quiz_data, candidate):
    show_df = pd.read_csv("users.csv")
    soham_df3 = pd.read_csv('admin.csv')
    
    
    
    show_df['Year of Experience'] = pd.to_numeric(show_df['Year of Experience'], errors='coerce').fillna(0)
    show_df['Quiz Score'] = pd.to_numeric(show_df['Quiz Score'], errors='coerce').fillna(0)
    show_df['Year of Experience'] = show_df['Year of Experience'].sort_values(ascending=True)
    show_df['matches'] = show_df['Aquired Skill'].apply(
        lambda x: int(any(skill in soham_df3['required_skills'].values for skill in x))
    )
    show_df['Performance'] = pd.to_numeric(show_df['matches'], errors='coerce') + pd.to_numeric(show_df['Quiz Score'], errors='coerce') + pd.to_numeric(show_df['Year of Experience'], errors='coerce')
    fig = px.bar(show_df,x="Name",y='Performance',title="Candidate Dash")
    
    
    
    if not n:
        return ""

    score = calculate_score(quiz_data)

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame(columns=['Name','Passing Year','Aquired Skill','Enter Collage','Year of Experience','Quiz Score','Score'])

    new_row = pd.DataFrame({
        'Name':[candidate.get('Name')],
        'Passing Year':[candidate.get('Passing Year')],
        'Aquired Skill':[candidate.get('Aquired Skill')],
        'Enter Collage':[candidate.get('Enter Collage')],
        'Year of Experience':[candidate.get('Year of Experience')],
        'Quiz Score':[score],
        'Score':[f"{score}/{len(questions)}"]
    })

    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(file_path, index=False)

    return f"Quiz submitted. Score: {score}/{len(questions)}"



if __name__ == "__main__":
    app.run(debug=True)
