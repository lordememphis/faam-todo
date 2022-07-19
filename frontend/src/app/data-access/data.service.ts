import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { PartialTaskEntity, TaskEntity } from "./models/task.model";

@Injectable({
  providedIn: "root",
})
export class DataService {
  private readonly baseUrl = "http://localhost:8001/api/v1";

  constructor(private http: HttpClient) {}

  createTask(payload: PartialTaskEntity) {
    return this.http.post<TaskEntity>(`${this.baseUrl}/tasks`, payload);
  }

  getTaskById(taskId: string) {
    return this.http.get<TaskEntity>(`${this.baseUrl}/tasks/${taskId}`);
  }

  getAllTasks() {
    return this.http.get<TaskEntity[]>(`${this.baseUrl}/tasks/all`);
  }

  updateTask(task: TaskEntity) {
    return this.http.put<TaskEntity>(`${this.baseUrl}/tasks/${task._id}`, task);
  }

  deleteTask(taskId: string) {
    return this.http.delete<string>(`${this.baseUrl}/tasks/${taskId}`);
  }
}
