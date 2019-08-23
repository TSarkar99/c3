import uuid


# this is originally the class "Pulse"
class Component:

    def __init__(
            self,
            name = " ",
            desc = " ",
            comment = " ",
            ):

        # make a random UUID which uniquely identifies/represents the component
        # https://docs.python.org/2/library/uuid.html#uuid.uuid4
        self.__uuid = uuid.uuid4()
        self.name = name
        self.desc = desc
        self.comment = comment

    def get_uuid(self):
        return self.__uuid

    def set_uuid(self, uuid):
        self.__uuid = uuid



class Signal_component(Component):
    """Represents a pulse.

    Parameters
    ----------
    shape : func
        Function handle to function specifying the exact shape of the pulse
    parameters : dict
        dictionary of the parameters needed for the shape-function to
        create the desired pulse
    bounds : dict
        boundaries of the parameters, i.e. technical limits of experimental
        setup or physical boundaries. needed for optimizer

    """

    def __init__(
            self,
            name = " ",
            desc = " ",
            comment = " ",
            shape = None,
            params = {},
            bounds = {},
            groups = []
            ):
        super().__init__(
            name = name,
            desc = desc,
            comment = comment
            )
        self.shape = shape
        self.params = params
        self.bounds = bounds
        self.groups = groups

    def get_shape_values(self, ts):
        return self.shape(ts, self.params)

class Physical_component(Component):
    def __init__(
            self,
            name = " ",
            desc = " ",
            comment = " ",
            hamiltonian = None,
            hilbert_dim = None
            ):
        super().__init__(
            name = name,
            desc = desc,
            comment = comment
            )
        self.hamiltonian = hamiltonian
        self.hilbert_dim = hilbert_dim
        self.values = {}

    def get_values(self):
        return self.values

    def get_hamiltonian(self, a):
        return self.hamiltonian(a, self.values)

class Qubit(Physical_component):
    def __init__(
            self,
            name = " ",
            desc = " ",
            comment = " ",
            hamiltonian = None,
            hilbert_dim = None,
            freq = None,
            delta = None,
            ):
        super().__init__(
            name = name,
            desc = desc,
            comment = comment,
            hamiltonian = hamiltonian,
            hilbert_dim = hilbert_dim
            )
        self.values['freq'] = freq
        self.values['delta'] = delta

class Resonator(Physical_component):
    def __init__(
            self,
            name = " ",
            desc = " ",
            comment = " ",
            hamiltonian = None,
            hilbert_dim = None,
            freq = None
            ):
        super().__init__(
            name = name,
            desc = desc,
            comment = comment,
            hamiltonian = hamiltonian,
            hilbert_dim = hilbert_dim
            )
        self.values['freq'] = freq

class Coupling(Physical_component):
    def __init__(
            self,
            name = " ",
            desc = " ",
            comment = " ",
            hamiltonian = None,
            hilbert_dim = None,
            connected = None,
            strength = None
            ):
        super().__init__(
            name = name,
            desc = desc,
            comment = comment,
            hamiltonian = hamiltonian,
            hilbert_dim = hilbert_dim
            )
        self.values['strength'] = strength
        self.connected = connected

class Drive(Physical_component):
    def __init__(
            self,
            name = " ",
            desc = " ",
            comment = " ",
            hamiltonian = None,
            hilbert_dim = None,
            connected = None
            ):
        super().__init__(
            name = name,
            desc = desc,
            comment = comment,
            hamiltonian = hamiltonian,
            hilbert_dim = hilbert_dim
            )
        self.connected = connected
