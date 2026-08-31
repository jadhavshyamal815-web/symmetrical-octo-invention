import { useState } from "react";
import "./App.css";

const workflows = [
  {
    id: "WF-001",
    name: "Product Review Workflow",
    status: "In Progress",
    tasks: 5,
  },
  {
    id: "WF-002",
    name: "Quality Assessment Workflow",
    status: "Pending",
    tasks: 3,
  },
  {
    id: "WF-003",
    name: "Regulatory Review Workflow",
    status: "Completed",
    tasks: 7,
  },
];

const taskData = {
  "WF-001": [
    "Collect product information",
    "Review analytical evidence",
    "Check quality documentation",
    "Review study results",
    "Prepare assessment",
  ],
  "WF-002": [
    "Collect quality records",
    "Review test results",
    "Prepare quality summary",
  ],
  "WF-003": [
    "Review regulatory documents",
    "Check compliance records",
    "Review submitted evidence",
    "Identify missing information",
    "Complete regulatory assessment",
    "Prepare review report",
    "Finalize assessment",
  ],
};

function App() {
  const [selectedWorkflow, setSelectedWorkflow] = useState<string | null>(null);
  const [selectedTask, setSelectedTask] = useState<string | null>(null);
  const [assignedUser, setAssignedUser] = useState<string>("Not assigned");
const [selectedAssignee, setSelectedAssignee] = useState<string>("");
const users = [
  "Aadesh Vishwakarma",
  "Reviewer 1",
  "Reviewer 2",
  "Quality Analyst",
  "Regulatory Reviewer",
];

  const selectedTasks = selectedWorkflow
    ? taskData[selectedWorkflow as keyof typeof taskData]
    : [];

  return (
    <div className="app">
      <header className="header">
        <h1>Workflow Workspace</h1>
        <p>SETU PMC Capability — Frontend Demonstration</p>
      </header>

      <main className="content">
        <section>
          <h2>Workflows</h2>

          <div className="workflow-grid">
            {workflows.map((workflow) => (
              <div className="workflow-card" key={workflow.id}>
                <h3>{workflow.name}</h3>

                <p>
                  <strong>Workflow ID:</strong> {workflow.id}
                </p>

                <p>
                  <strong>Status:</strong> {workflow.status}
                </p>

                <p>
                  <strong>Tasks:</strong> {workflow.tasks}
                </p>

                <button
                  onClick={() => setSelectedWorkflow(workflow.id)}
                >
                  Select Workflow
                </button>
              </div>
            ))}
          </div>
        </section>

        {selectedWorkflow && (
          <section className="task-board">
            <div className="task-board-header">
              <div>
                <h2>Task Board</h2>
                <p>
                  Selected Workflow: <strong>{selectedWorkflow}</strong>
                </p>
              </div>

              <button
                className="close-button"
                onClick={() => setSelectedWorkflow(null)}
              >
                Close
              </button>
            </div>

            <div className="task-list">
              {selectedTasks.map((task, index) => (
                <div
  className="task-card"
  key={index}
  onClick={() => setSelectedTask(task)}
  role="button"
  tabIndex={0}
  onKeyDown={(event) => {
    if (event.key === "Enter" || event.key === " ") {
      setSelectedTask(task);
    }
  }}
>
  <input
    type="checkbox"
    id={`task-${index}`}
    onClick={(event) => event.stopPropagation()}
  />

  <label htmlFor={`task-${index}`}>
    <strong>Task {index + 1}</strong>
    <span>{task}</span>
  </label>
</div>
              ))}
            </div>
          </section>
        )}
        {selectedTask && (
  <aside className="task-drawer">
    <div className="drawer-header">
      <h2>Task Details</h2>

      <button
        className="close-button"
        onClick={() => setSelectedTask(null)}
      >
        Close
      </button>
    </div>

    <div className="drawer-content">
      <h3>{selectedTask}</h3>

      <p>
        <strong>Status:</strong> Pending
      </p>

      <p>
        <strong>Priority:</strong> Normal
      </p>

     <p>
  <strong>Assigned To:</strong> {assignedUser}
</p>

<div className="assignment-panel">
  <h3>Assignment</h3>

  <label htmlFor="assignee">
    Assign To:
  </label>

  <select
    id="assignee"
    value={selectedAssignee}
    onChange={(event) => setSelectedAssignee(event.target.value)}
  >
    <option value="">Select a person</option>

    {users.map((user) => (
      <option key={user} value={user}>
        {user}
      </option>
    ))}
  </select>

  <button
    className="assign-button"
    disabled={!selectedAssignee}
    onClick={() => setAssignedUser(selectedAssignee)}
  >
    Assign Task
  </button>
</div>

      <p>
        <strong>Description:</strong>
      </p>

      <p>
        Review and complete this task according to the workflow requirements.
      </p>
    </div>
  </aside>
)}
      </main>
    </div>
  );
}

export default App;