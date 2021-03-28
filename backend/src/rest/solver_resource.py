from dataclasses import asdict

from flask import jsonify
from src.interface.usecase import SolverUsecase


class SolverResource:
    solver_usecase: SolverUsecase

    def __init__(self, solver_usecase: SolverUsecase):
        self.solver_usecase = solver_usecase

    def solve(self, room_id: str, time_limit: int):
        setlist = self.solver_usecase.solve(room_id, time_limit)
        return jsonify(asdict(setlist))
