from abc import ABC, abstractmethod
from typing import Optional
from week4.model.location import Location


class Environment(ABC):
    @abstractmethod
    def clear(self):
        """Clear the environment of all agents."""
        pass

    @abstractmethod
    def get_agent(self, location):
        """Get the agent at a specific location.

        :param location: The location to get the agent from.
        :return: The agent at the given location, or None if no agent is present.
        """
        pass

    @abstractmethod
    def set_agent(self, agent, location):
        """Set an agent at a specific location.

        :param agent: The agent to set in the environment.
        :param location: The location to place the agent.
        """
        pass

    @abstractmethod
    def get_height(self):
        """Get the height of the environment.

        :return: The height of the environment.
        """
        pass

    @abstractmethod
    def get_width(self):
        """Get the width of the environment.

        :return: The width of the environment.
        """
        pass
