"""
Code generated by a tool. DO NOT EDIT.
https://sqldalmaker.sourceforge.net/
"""

from dbal.task_li import TaskLi


class TasksDao:

    def __init__(self, ds):
        self.ds = ds

    def create_task(self, p):
        """
        (C)RUD: tasks
        Generated values are passed to DTO.
        :param p: Task
        :return: None
        :raises Exception: if no rows inserted.
        """
        sql = """insert into tasks (p_id, t_priority, t_date, t_subject, t_comments) values (?, ?, ?, ?, ?)"""
        _ai_values = [["t_id", None]]
        self.ds.insert_row(sql, [p.p_id, p.t_priority, p.t_date, p.t_subject, p.t_comments], _ai_values)
        p.t_id = _ai_values[0][1]

    def read_task(self, t_id, obj):
        """
        C(R)UD: tasks
        :param t_id: int
        :param obj: Task
        :return: None on success or error string
        """
        sql = """select * from tasks where t_id=?"""
        row = self.ds.query_row(sql, [t_id])
        if isinstance(row, str):
            return row
        obj.t_id = row["t_id"]  # t <- t
        obj.p_id = row["p_id"]  # t <- t
        obj.t_priority = row["t_priority"]  # t <- t
        obj.t_date = row["t_date"]  # t <- t
        obj.t_subject = row["t_subject"]  # t <- t
        obj.t_comments = row["t_comments"]  # t <- t

    def delete_task(self, t_id):
        """
        CRU(D): tasks
        :param t_id: int
        :return: int (the number of affected rows)
        """
        sql = """delete from tasks where t_id=?"""
        return self.ds.exec_dml(sql, [t_id])

    def get_project_tasks(self, p_id):
        """
        :param p_id: str
        :return: list[TaskLi]
        """
        sql = """select t_id, t_date, t_subject, t_priority 
                from tasks 
                where p_id = ?"""

        _res = []

        def _map_cb(row):
            _obj = TaskLi()
            _obj.t_id = row["t_id"]  # q <- q
            _obj.t_date = row["t_date"]  # q <- q
            _obj.t_subject = row["t_subject"]  # q <- q
            _obj.t_priority = row["t_priority"]  # q <- q
            _res.append(_obj)

        self.ds.query_all_rows(sql, [p_id], _map_cb)
        return _res

    def update_task(self, t_priority, t_date, t_subject, t_comments, t_id):
        """
        :param t_priority: str
        :param t_date: str
        :param t_subject: str
        :param t_comments: str
        :param t_id: str
        :return: int (the number of affected rows)
        """
        sql = """update tasks set t_priority=?, t_date=?, t_subject=?, t_comments=? where t_id=?"""
        return self.ds.exec_dml(sql, [t_priority, t_date, t_subject, t_comments, t_id])
