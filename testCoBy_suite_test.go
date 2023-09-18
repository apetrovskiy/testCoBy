package testCoBy_test

import (
	"testing"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

func TestTestCoBy(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "TestCoBy Suite")
}
