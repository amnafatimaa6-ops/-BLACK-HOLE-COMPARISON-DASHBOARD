import numpy as np

class ParticleSimulator:

    def __init__(self, n_particles=300):

        self.n = n_particles

        self.r = np.random.uniform(2.5,5,self.n)

        self.theta = np.random.uniform(
            0,
            2*np.pi,
            self.n
        )

    def schwarzschild(self):

        self.theta += 0.008/self.r

        x=self.r*np.cos(self.theta)
        y=self.r*np.sin(self.theta)

        return x,y

    def kerr(self):

        self.theta += 0.025/self.r

        x=self.r*np.cos(self.theta)
        y=self.r*np.sin(self.theta)

        return x,y

    def reissner(self):

        pulse=.12*np.sin(self.theta*4)

        x=(self.r+pulse)*np.cos(self.theta)
        y=(self.r+pulse)*np.sin(self.theta)

        self.theta+=0.01

        return x,y

    def kerr_newman(self):

        pulse=.18*np.sin(self.theta*5)

        self.theta+=0.03/self.r

        x=(self.r+pulse)*np.cos(self.theta)
        y=(self.r+pulse)*np.sin(self.theta)

        return x,y
