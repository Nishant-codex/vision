import pytest
from brainscore_vision.benchmarks.nod_imagenet_v1v2_vwfa_ppa_ffa import (
    NeuralData, StimulusSet, Benchmark
)

def test_neural_data_has_correct_dimensions():
    neural = NeuralData()
    assert neural.shape[0] > 0  # presentations
    assert neural.shape[1] > 0  # neuroids (voxels/vertices)

def test_stimulus_set_has_mapping():
    stim = StimulusSet()
    assert len(stim.manifest) > 0

def test_benchmark_returns_score():
    benchmark = Benchmark()
    score = benchmark.score(model="alexnet")
    assert score is not None