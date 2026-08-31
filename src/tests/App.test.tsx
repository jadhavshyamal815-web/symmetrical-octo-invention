import { render, screen, fireEvent } from "@testing-library/react";
import { describe, expect, test } from "vitest";
import App from "../App";

describe("Workflow Workspace", () => {
  test("displays the Workflow Workspace heading", () => {
    render(<App />);

    expect(screen.getByText("Workflow Workspace")).toBeTruthy();
  });

  test("displays all three workflows", () => {
    render(<App />);

   expect(screen.getAllByText("Product Review Workflow").length).toBeGreaterThan(0);
    expect(screen.getAllByText("Quality Assessment Workflow").length).toBeGreaterThan(0);
    expect(screen.getAllByText("Regulatory Review Workflow").length).toBeGreaterThan(0);
  });

  test("can select Product Review Workflow", () => {
    render(<App />);

    const buttons = screen.getAllByRole("button", {
      name: "Select Workflow",
    });

    fireEvent.click(buttons[0]);

    expect(screen.getAllByText("WF-001").length).toBeGreaterThan(0);
  });

  test("shows Product Review tasks", () => {
    render(<App />);

    const buttons = screen.getAllByRole("button", {
      name: "Select Workflow",
    });

    fireEvent.click(buttons[0]);

    expect(
      screen.getByText("Review analytical evidence")
    ).toBeTruthy();

    expect(
      screen.getByText("Check quality documentation")
    ).toBeTruthy();

    expect(
      screen.getByText("Review study results")
    ).toBeTruthy();

    expect(
      screen.getByText("Prepare assessment")
    ).toBeTruthy();
  });

  test("opens task details", () => {
    render(<App />);

    const buttons = screen.getAllByRole("button", {
      name: "Select Workflow",
    });

    fireEvent.click(buttons[0]);

    const tasks = screen.getAllByText("Collect product information");
fireEvent.click(tasks[tasks.length - 1]);

    expect(screen.getByText("Task Details")).toBeTruthy();

    expect(
      screen.getAllByText("Collect product information")
    ).toBeTruthy();
  });

  test("displays assignment controls", () => {
    render(<App />);

    const buttons = screen.getAllByRole("button", {
      name: "Select Workflow",
    });

    fireEvent.click(buttons[0]);

    const taskTexts = screen.getAllByText("Collect product information");

    fireEvent.click(taskTexts[taskTexts.length - 1]);

    expect(screen.getByText("Assignment")).toBeTruthy();

    expect(
      screen.getByRole("button", {
        name: "Assign Task",
      })
    ).toBeTruthy();
  });
});