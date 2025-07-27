import torch
from torch import nn, Tensor, LongTensor
from torch.optim import Adam

from transformers import PreTrainedTokenizer

from typing import Literal

# 구현하세요!
def generate_contexts_and_targets(
    tokens: LongTensor,
    window_size: int) -> tuple[LongTensor, LongTensor]:
    contexts = []
    targets: LongTensor = tokens[window_size: len(tokens)-window_size] # type:ignore
    for i in range(window_size, len(tokens) - window_size):
        context = tokens[i - window_size:i].tolist() + tokens[i + 1:i + window_size + 1].tolist() # type:ignore
        contexts.append(context)
    return torch.LongTensor(contexts), targets


class Word2Vec(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        d_model: int,
        window_size: int,
        method: Literal["cbow", "skipgram"]
    ) -> None:
        super().__init__()
        self.embeddings = nn.Embedding(vocab_size, d_model)
        self.weight = nn.Linear(d_model, vocab_size, bias=False)
        self.window_size = window_size
        self.method = method
        # 구현하세요!
        
    def embeddings_weight(self) -> Tensor:
        return self.embeddings.weight.detach()

    def fit(
        self,
        corpus: list[str],
        tokenizer: PreTrainedTokenizer,
        lr: float,
        num_epochs: int
    ) -> None:
        criterion = nn.CrossEntropyLoss()
        optimizer = Adam(self.parameters(), lr=lr)
        # 구현하세요!
        for epoch in range(num_epochs):
            for sentence in corpus:
                tokens = tokenizer(sentence, return_tensors="pt", truncation=True, padding=True)
                input_ids = tokens["input_ids"].squeeze(0)  # type:ignore

                contexts, targets = generate_contexts_and_targets(input_ids, self.window_size)
                
                if contexts.size(0) == 0 or targets.size(0) == 0:
                    continue
                if self.method == "cbow":
                    self._train_cbow(contexts, targets, criterion, optimizer)
                elif self.method == "skipgram":
                    self._train_skipgram(contexts, targets, criterion, optimizer)
        
            print(f"Epoch {epoch + 1}/{num_epochs} completed.")
            

    def _train_cbow(
        self,
        # 구현하세요!
        contexts: LongTensor,
        targets: LongTensor,
        criterion: nn.Module,
        optimizer: Adam
    ) -> None:
        # 구현하세요!
        contexts_emb = self.embeddings(contexts)
        contexts_emb = contexts_emb.mean(dim=1)
        logits = self.weight(contexts_emb)
        loss = criterion(logits, targets)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

    def _train_skipgram(
        self,
        # 구현하세요!
        contexts: LongTensor,
        targets: LongTensor,
        criterion: nn.Module,
        optimizer: Adam
    ) -> None:
        # 구현하세요!
        targets_emb = self.embeddings(targets)
        logits = self.weight(targets_emb)

        total_loss = torch.tensor(0, dtype=torch.float32, requires_grad=True)
        context_length = contexts.size(1)

        for i in range(context_length):
            context = contexts[:, i]
            loss = criterion(logits, context)
            total_loss.data += loss

        avg_loss = total_loss / context_length
        avg_loss.backward()
        optimizer.step()
        optimizer.zero_grad()

    # 구현하세요!
    pass