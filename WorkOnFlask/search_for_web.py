from flask import Flask,render_template,request,escape
from vsearch import search4letter

app=Flask(__name__)


def log_request(req:'flask_request',res:str)->None:
    with open('vsearch.log','a') as task:
        print(req.form, req.remote_addr, req.user_agent, res,file=task,sep="|") 


@app.route('/search4',methods=['POST'])
def search4() -> 'html':
    phrase=request.form['phrase']
    letters=request.form['letters']
    the_title="Here Is The Result"
    result=str(search4letter(phrase,letters))
    log_request(request,result)
    return render_template('result.html',
                            the_phrase=phrase,
                            the_letters=letters,
                            the_title=the_title,
                            the_results=result)
@app.route('/')
@app.route('/entry')
def form_entry() -> 'html':
    return render_template('entry.html',
                            the_title="Welcome to search4letters on web")
@app.route('/viewlog')
def view_log()->'html':
    contents=[]
    headings=['Form Data','Remote Address','User Agent','Results']
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
        #escape keyword will help browser to render HTML TAGS TOO
        
        
    return render_template('view_log.html',
                           the_row_titles=headings,
                           the_title="View Log",
                           the_data=contents)

if __name__=='__main__':
        app.run(debug=True)
