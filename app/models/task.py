from app import db
from datetime import datetime

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)
    # FOR ONE TO MANY RELATIONSHIP
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id'))
    goal = db.relationship("Goal", back_populates="tasks")

    def to_dict(self):

        task_as_dict = {}
        task_as_dict["id"]=self.task_id
        task_as_dict["title"]=self.title
        task_as_dict["description"]=self.description
        task_as_dict["is_complete"]=self.completed_at != None
        
        if self.goal_id:
            task_as_dict["goal_id"]=self.goal_id

        return task_as_dict
    
    @classmethod
    def from_dict(cls, task_data):
        new_task = Task(title=task_data['title'],
                        description=task_data['description'],
                        completed_at=task_data.get('completed_at'))
        
        return new_task
        