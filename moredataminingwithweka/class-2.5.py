# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# More Data Mining with Weka - Class 2.5
# Copyright (C) 2014 Fracpete (fracpete at gmail dot com)

# TODO
# wherever your datasets are located
data_dir = "/some/where/data"

import os
import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import Classifier, Evaluation, PredictionOutput
from weka.core.classes import Random
import weka.plot.classifiers as plc

jvm.start()

# load weather.nominal
fname = data_dir + os.sep + "weather.nominal.arff"
print("\nLoading dataset: " + fname + "\n")
loader = Loader(classname="weka.core.converters.ArffLoader")
data = loader.load_file(fname)
data.set_class_index(data.num_attributes() - 1)

# cross-validate NaiveBayes
cls = Classifier(classname="weka.classifiers.bayes.NaiveBayes")
pout = PredictionOutput(classname="weka.classifiers.evaluation.output.prediction.PlainText", options=["-distribution"])
evl = Evaluation(data)
evl.crossvalidate_model(cls, data, 10, Random(1), pout)
print(evl.to_summary())
print(evl.to_matrix())
print(pout)
plc.plot_roc(evl, wait=True)

jvm.stop()