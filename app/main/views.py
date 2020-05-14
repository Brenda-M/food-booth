from flask import render_template
from . import main


# your views go here i.e for home,about
@main.route("/")
def index():
    return "<h1>Hello World</h1>"


@main.route("/about")
def about():
    pass


    form = PitchForm()
    my_upvotes = Upvote.query.filter_by(pitch_id=Pitch.id)

 

@main.route('/user/new/<int:user_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = userForm()
    user = user.query.get(pitch_id)

    if form.validate_on_submit():
        comment = form.comment.data
         
        # Updated comment instance
        new_user = user(user=user,user_c=current_user._get_current_object().id, pitch_id=pitch_id)

        # save comment method
        new_comment.save_comment()
        return redirect(url_for('.new_comment',pitch_id = pitch_id ))
    all_user = Comment.query.filter_by(pitch_id=pitch_id).all()
    return render_template('display.html', form=form, users=all_users)
