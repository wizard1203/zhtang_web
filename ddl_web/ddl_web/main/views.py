from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app, request, flash

from . import main
# from .forms import NameForm
from .forms import Form_create_user, Form_query_dataset, Form_submit_job, Form_query_job, Form_kill_job

from .. import db
from ..models import User
import os

@main.route('/', methods=['GET', 'POST'])
def index():
    form_create_user = Form_create_user()
    form_query_dataset = Form_query_dataset()
    form_submit_job = Form_submit_job()
    form_query_job = Form_query_job()
    form_kill_job = Form_kill_job()

    return render_template('index.html', name=session.get('name'),
            known=session.get('known', False), current_time=datetime.utcnow(),
            form_create_user=form_create_user, form_query_dataset=form_query_dataset,
            form_submit_job=form_submit_job, form_query_job=form_query_job,
            form_kill_job=form_kill_job)

@main.route('/user/create', methods=['GET', 'POST'])
def create_user():
    form_create_user = Form_create_user()
    form_query_dataset = Form_query_dataset()
    form_submit_job = Form_submit_job()
    form_query_job = Form_query_job()
    form_kill_job = Form_kill_job()

    # print(request.method) #
    # print(request.url) #
    # print(request.cookies) #
    # print(request.path)  # 
    # print(request.args) #
    # print(request.args.get("id")) #
    # print(request.args["name"]) #
    # print(request.args.to_dict()) #

    if form_create_user.validate_on_submit():
        print('create_user============')
        current_app.config['LOGGER'].info('create_user============')
        # user = User.query.filter_by(username=form.name.data).first()
        # if user is None:
        #     user = User(username=form.name.data)
        #     db.session.add(user)
        #     db.session.commit()
        #     session['known'] = False
        #     if current_app.config['FLASKY_ADMIN']:
        #         send_email(current_app.config['FLASKY_ADMIN'], 'New User',
        #                    'mail/new_user', user=user)
        # else:
        #     session['known'] = True
        # session['name'] = form.name.data
        return redirect(url_for('main.index'))
    # return render_template('index.html', form=form, name=session.get('name'),
    #         known=session.get('known', False), current_time=datetime.utcnow())
    return render_template('index.html', name=session.get('name'),
            known=session.get('known', False), current_time=datetime.utcnow(),
            form_create_user=form_create_user, form_query_dataset=form_query_dataset,
            form_submit_job=form_submit_job, form_query_job=form_query_job,
            form_kill_job=form_kill_job)

@main.route('/api/dataset/query', methods=['GET', 'POST'])
def query_dataset():
    form_create_user = Form_create_user()
    form_query_dataset = Form_query_dataset()
    form_submit_job = Form_submit_job()
    form_query_job = Form_query_job()
    form_kill_job = Form_kill_job()

    if form_query_dataset.validate_on_submit():
        print('query_dataset============')
        current_app.config['LOGGER'].info('query_dataset============')
        # user = User.query.filter_by(username=form.name.data).first()
        # if user is None:
        #     user = User(username=form.name.data)
        #     db.session.add(user)
        #     db.session.commit()
        #     session['known'] = False
        #     if current_app.config['FLASKY_ADMIN']:
        #         send_email(current_app.config['FLASKY_ADMIN'], 'New User',
        #                    'mail/new_user', user=user)
        # else:
        #     session['known'] = True
        # session['name'] = form.name.data
        return redirect(url_for('main.index'))
    # return render_template('index.html', form=form, name=session.get('name'),
    #         known=session.get('known', False), current_time=datetime.utcnow())
    return render_template('index.html', name=session.get('name'),
            known=session.get('known', False), current_time=datetime.utcnow(),
            form_create_user=form_create_user, form_query_dataset=form_query_dataset,
            form_submit_job=form_submit_job, form_query_job=form_query_job,
            form_kill_job=form_kill_job)

@main.route('/api/job/submit', methods=['GET', 'POST'])
def submit_job():
    form_create_user = Form_create_user()
    form_query_dataset = Form_query_dataset()
    form_submit_job = Form_submit_job()
    form_query_job = Form_query_job()
    form_kill_job = Form_kill_job()
    print('receive file============')
    current_app.config['LOGGER'].info('receive file============')
    if form_submit_job.validate_on_submit():
        user_code = form_submit_job.job_code.data
        # user_code = request.files['file']
        print(user_code)
        print('receive file============')
        current_app.config['LOGGER'].info('receive file============')
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'upload_files', user_code.filename)
        file_dir = os.path.join(basepath, 'upload_files')
        current_app.config['LOGGER'].info(upload_path)        
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        user_code.save(upload_path)
        flash('Upload Success')
        # user = User.query.filter_by(username=form.name.data).first()
        # if user is None:
        #     user = User(username=form.name.data)
        #     db.session.add(user)
        #     db.session.commit()
        #     session['known'] = False
        #     if current_app.config['FLASKY_ADMIN']:
        #         send_email(current_app.config['FLASKY_ADMIN'], 'New User',
        #                    'mail/new_user', user=user)
        # else:
        #     session['known'] = True
        # session['name'] = form.name.data
        return redirect(url_for('main.index'))
        #return "Upload success"
    else:
        print('not receive file============')
        current_app.config['LOGGER'].info('not receive file============')        
    # return render_template('index.html', form=form, name=session.get('name'),
    #         known=session.get('known', False), current_time=datetime.utcnow())
    return render_template('index.html', name=session.get('name'),
            known=session.get('known', False), current_time=datetime.utcnow(),
            form_create_user=form_create_user, form_query_dataset=form_query_dataset,
            form_submit_job=form_submit_job, form_query_job=form_query_job,
            form_kill_job=form_kill_job)

@main.route('/api/job/query', methods=['GET', 'POST'])
def query_job():
    form_create_user = Form_create_user()
    form_query_dataset = Form_query_dataset()
    form_submit_job = Form_submit_job()
    form_query_job = Form_query_job()
    form_kill_job = Form_kill_job()

    if form_query_job.validate_on_submit():
        print('query_job============')
        current_app.config['LOGGER'].info('query_job============')
        # user = User.query.filter_by(username=form.name.data).first()
        # if user is None:
        #     user = User(username=form.name.data)
        #     db.session.add(user)
        #     db.session.commit()
        #     session['known'] = False
        #     if current_app.config['FLASKY_ADMIN']:
        #         send_email(current_app.config['FLASKY_ADMIN'], 'New User',
        #                    'mail/new_user', user=user)
        # else:
        #     session['known'] = True
        # session['name'] = form.name.data
        return redirect(url_for('main.index'))
    # return render_template('index.html', form=form, name=session.get('name'),
    #         known=session.get('known', False), current_time=datetime.utcnow())
    return render_template('index.html', name=session.get('name'),
            known=session.get('known', False), current_time=datetime.utcnow(),
            form_create_user=form_create_user, form_query_dataset=form_query_dataset,
            form_submit_job=form_submit_job, form_query_job=form_query_job,
            form_kill_job=form_kill_job)

@main.route('/api/job/kill', methods=['GET', 'POST'])
def kill_job():
    form_create_user = Form_create_user()
    form_query_dataset = Form_query_dataset()
    form_submit_job = Form_submit_job()
    form_query_job = Form_query_job()
    form_kill_job = Form_kill_job()

    if form_kill_job.validate_on_submit():
        print('kill_job============')
        current_app.config['LOGGER'].info('kill_job============')
        # user = User.query.filter_by(username=form.name.data).first()
        # if user is None:
        #     user = User(username=form.name.data)
        #     db.session.add(user)
        #     db.session.commit()
        #     session['known'] = False
        #     if current_app.config['FLASKY_ADMIN']:
        #         send_email(current_app.config['FLASKY_ADMIN'], 'New User',
        #                    'mail/new_user', user=user)
        # else:
        #     session['known'] = True
        # session['name'] = form.name.data
        return redirect(url_for('main.index'))
    # return render_template('index.html', form=form, name=session.get('name'),
    #         known=session.get('known', False), current_time=datetime.utcnow())
    return render_template('index.html', name=session.get('name'),
            known=session.get('known', False), current_time=datetime.utcnow(),
            form_create_user=form_create_user, form_query_dataset=form_query_dataset,
            form_submit_job=form_submit_job, form_query_job=form_query_job,
            form_kill_job=form_kill_job)
