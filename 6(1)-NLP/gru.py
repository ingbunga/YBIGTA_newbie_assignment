import torch
from torch import nn, Tensor


class GRUCell(nn.Module):
    def __init__(self, input_size: int, hidden_size: int) -> None:
        super().__init__()
        # 구현하세요!
        self.input_size = input_size
        self.hidden_size = hidden_size

        self.W_iz = nn.Linear(input_size, hidden_size)
        self.W_ir = nn.Linear(input_size, hidden_size)
        self.W_in = nn.Linear(input_size, hidden_size)
        self.W_hz = nn.Linear(hidden_size, hidden_size)
        self.W_hr = nn.Linear(hidden_size, hidden_size)
        self.W_hn = nn.Linear(hidden_size, hidden_size)
        

    def forward(self, x: Tensor, h: Tensor) -> Tensor:
        # 구현하세요!
        z = torch.sigmoid(self.W_iz(x) + self.W_hz(h))
        r = torch.sigmoid(self.W_ir(x) + self.W_hr(h))
        n = torch.tanh(self.W_in(x) + r * self.W_hn(h))
        h_next = (1 - z) * n + z * h

        return h_next


class GRU(nn.Module):
    def __init__(self, input_size: int, hidden_size: int) -> None:
        super().__init__()
        self.hidden_size = hidden_size
        self.cell = GRUCell(input_size, hidden_size)
        # 구현하세요!
        self.fc = nn.Linear(hidden_size, input_size)

    def forward(self, inputs: Tensor) -> Tensor:
        # 구현하세요!
        batch_size, seq_len, _ = inputs.size()
        h = torch.zeros(batch_size, self.hidden_size, device=inputs.device)

        for t in range(seq_len):
            h = self.cell(inputs[:, t, :], h)

        output = self.fc(h)
        return output