/*
Copyright 2024 The Kubeflow Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package controllerv2

import (
	"github.com/onsi/ginkgo/v2"
	"github.com/onsi/gomega"
	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/utils/ptr"
	"sigs.k8s.io/controller-runtime/pkg/client"

	kubeflowv2 "github.com/kubeflow/training-operator/pkg/apis/kubeflow.org/v2alpha1"
	"github.com/kubeflow/training-operator/test/integration/framework"
)

var _ = ginkgo.Describe("TrainJob controller", ginkgo.Ordered, func() {
	var ns *corev1.Namespace

	ginkgo.BeforeAll(func() {
		fwk = &framework.Framework{}
		cfg = fwk.Init()
		ctx, k8sClient = fwk.RunManager(cfg)
	})
	ginkgo.AfterAll(func() {
		fwk.Teardown()
	})

	ginkgo.BeforeEach(func() {
		ns = &corev1.Namespace{
			TypeMeta: metav1.TypeMeta{
				APIVersion: corev1.SchemeGroupVersion.String(),
				Kind:       "Namespace",
			},
			ObjectMeta: metav1.ObjectMeta{
				GenerateName: "trainjob-",
			},
		}
		gomega.Expect(k8sClient.Create(ctx, ns)).To(gomega.Succeed())
	})

	ginkgo.When("Reconciling TrainJob", func() {
		ginkgo.AfterEach(func() {
			gomega.Expect(k8sClient.DeleteAllOf(ctx, &kubeflowv2.TrainJob{}, client.InNamespace(ns.Name))).Should(gomega.Succeed())
		})

		ginkgo.It("Should succeed to create TrainJob", func() {
			trainJob := &kubeflowv2.TrainJob{
				TypeMeta: metav1.TypeMeta{
					APIVersion: kubeflowv2.SchemeGroupVersion.String(),
					Kind:       "TrainJob",
				},
				ObjectMeta: metav1.ObjectMeta{
					Name:      "alpha",
					Namespace: ns.Name,
				},
			}
			gomega.Expect(k8sClient.Create(ctx, trainJob)).Should(gomega.Succeed())
		})
	})

	ginkgo.When("TrainJob CR Validation", func() {
		ginkgo.AfterEach(func() {
			gomega.Expect(k8sClient.DeleteAllOf(ctx, &kubeflowv2.TrainJob{}, client.InNamespace(ns.Name))).Should(
				gomega.Succeed())
		})

		ginkgo.It("Should succeed in creating TrainJob", func() {

			managedBy := "kubeflow.org/trainjob-controller"

			trainingRuntimeRef := kubeflowv2.RuntimeRef{
				Name:     "TorchRuntime",
				APIGroup: ptr.To(kubeflowv2.GroupVersion.Group),
				Kind:     ptr.To(kubeflowv2.TrainingRuntimeKind),
			}
			jobSpec := kubeflowv2.TrainJobSpec{
				RuntimeRef: trainingRuntimeRef,
				ManagedBy:  &managedBy,
			}
			trainJob := &kubeflowv2.TrainJob{
				TypeMeta: metav1.TypeMeta{
					APIVersion: kubeflowv2.SchemeGroupVersion.String(),
					Kind:       kubeflowv2.TrainJobKind,
				},
				ObjectMeta: metav1.ObjectMeta{
					GenerateName: "valid-trainjob-",
					Namespace:    ns.Name,
				},
				Spec: jobSpec,
			}

			err := k8sClient.Create(ctx, trainJob)
			gomega.Expect(err).Should(gomega.Succeed())
		})

		ginkgo.It("Should fail in creating TrainJob with invalid spec.managedBy", func() {
			managedBy := "invalidManagedBy"
			jobSpec := kubeflowv2.TrainJobSpec{
				ManagedBy: &managedBy,
			}
			trainJob := &kubeflowv2.TrainJob{
				TypeMeta: metav1.TypeMeta{
					APIVersion: kubeflowv2.SchemeGroupVersion.String(),
					Kind:       kubeflowv2.TrainJobKind,
				},
				ObjectMeta: metav1.ObjectMeta{
					Name:      "invalid-trainjob",
					Namespace: ns.Name,
				},
				Spec: jobSpec,
			}
			gomega.Expect(k8sClient.Create(ctx, trainJob)).To(gomega.MatchError(
				gomega.ContainSubstring("spec.managedBy: Invalid value")))
		})

		ginkgo.It("Should fail in updating spec.managedBy", func() {

			managedBy := "kubeflow.org/trainjob-controller"

			trainingRuntimeRef := kubeflowv2.RuntimeRef{
				Name:     "TorchRuntime",
				APIGroup: ptr.To(kubeflowv2.GroupVersion.Group),
				Kind:     ptr.To(kubeflowv2.TrainingRuntimeKind),
			}
			jobSpec := kubeflowv2.TrainJobSpec{
				RuntimeRef: trainingRuntimeRef,
				ManagedBy:  &managedBy,
			}
			trainJob := &kubeflowv2.TrainJob{
				TypeMeta: metav1.TypeMeta{
					APIVersion: kubeflowv2.SchemeGroupVersion.String(),
					Kind:       kubeflowv2.TrainJobKind,
				},
				ObjectMeta: metav1.ObjectMeta{
					Name:      "job-with-failed-update",
					Namespace: ns.Name,
				},
				Spec: jobSpec,
			}

			gomega.Expect(k8sClient.Create(ctx, trainJob)).Should(gomega.Succeed())
			updatedManagedBy := "kueue.x-k8s.io/multikueue"
			jobSpec.ManagedBy = &updatedManagedBy
			trainJob.Spec = jobSpec
			gomega.Expect(k8sClient.Update(ctx, trainJob)).To(gomega.MatchError(
				gomega.ContainSubstring("ManagedBy value is immutable")))
		})
	})
})
