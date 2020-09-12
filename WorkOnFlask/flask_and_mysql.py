from flask import Flask,render_template,request,escape,redirect
from vsearch import search4letter
from DBcm import UseDatabase,ConnectionError,CredentialError,SQLException

app=Flask(__name__)
app.config['dbconfig']={
      'host':'localhost',
      'user':'user',
      'password':'john',
      'database':'searchlog', 
    }

def log_request(req:'flask_request',res:str)->None:
     with UseDatabase(app.config['dbconfig']) as cursor:
            sql="""insert into logs
                   (phrase,letter,ip,browser_string,results)
                   values (%s,%s,%s,%s,%s)    
                """
            cursor.execute(sql,(req.form['phrase'],req.form['letters'],
                                req.remote_addr,req.user_agent.browser,
                                str(res)))

      
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
    try:
          headings=['Phrase','Letters','Remote Address','User Agent','Results']
          with UseDatabase(app.config['dbconfig']) as cursor:
              _sql='''Select phrase,letter,ip,browser_string,results from logs'''
              cursor.execute(_sql)
              data=cursor.fetchall()
          return render_template('view_log.html',
                                 the_row_titles=headings,
                                 the_title="View Log",
                                 the_data=data)
    #This Exception raised if mysql stops in service
    except ConnectionError as err:
            #write the handler here
            return 'Connection Error'
    #This Exception catch will be raised if a userName/password is incorrect 
    except CredentialError as err:
          return 'Credential Error'
    #This  Exception catch will be raised if sql statement is not correct
    except SQLException as err:
          return redirect('/')

if __name__=='__main__':
        app.run(debug=True)
