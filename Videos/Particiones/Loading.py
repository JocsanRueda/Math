from manim import *


class PensandoGenial(Scene):
    def construct(self):
        # Crear planetas animados (círculos simulando planetas)
        planetas = VGroup(
            Circle(radius=0.2, color=GREEN),
            Circle(radius=0.3, color=GRAY),
            Circle(radius=0.4, color=TEAL),
            Circle(radius=0.2, color=BLUE),
        )

        # Posicionar los planetas en forma de interrogación
        planetas.arrange(RIGHT, buff=0.2)
        planetas.move_to(ORIGIN)

        # Añadir los dientes simulando satélites orbitando alrededor de los planetas
        satelites = VGroup(
            self.create_satelites(planetas[0], 5, color=YELLOW),
            self.create_satelites(planetas[1], 2, color=BLUE),
            self.create_satelites(planetas[2], 1, color=RED),
            self.create_satelites(planetas[3], 4, color=GREEN),
        )

        # Añadir los planetas y los satélites a la escena
        self.play(Create(planetas), Create(satelites))

        # Añadir una animación de rotación continua a los planetas y los satélites
        self.play(
            Rotate(planetas, 5 * PI, about_point=ORIGIN),
            *[Rotate(obj,np.random.uniform(4, 5)*PI, about_point=ORIGIN) for obj in planetas],
            Rotate(satelites, 5 * PI, about_point=ORIGIN),
            run_time=15,
            rate_func=linear
        )
        self.play(
            Rotate(planetas, 5 * PI, about_point=ORIGIN),
            *[Rotate(obj,np.random.uniform(4, 5)*PI, about_point=ORIGIN) for obj in planetas],
            Rotate(satelites, 5 * PI, about_point=ORIGIN),
            run_time=15,
            rate_func=linear
        )

        # Añadir una simulación de atracción gravitacional entre los planetas
        self.gravity_simulation(planetas, satelites, G=5.0)

        # Mostrar la escena durante unos segundos antes de finalizar
        self.wait(2)

    def create_satelites(self, planeta, cantidad, color):
        satelites = VGroup()
        for i in range(cantidad):
            satelite = Circle(
                radius=np.random.uniform(0.03, 0.05),
                color=color,
                fill_opacity=1,
                stroke_width=0,
            )
            angle = 2 * PI * i / cantidad
            separation = np.random.uniform(0.2, 2)  # Separación entre satélites
            initial_position = (
                planeta.get_center()
                + separation
                * planeta.get_height()
                * np.array([np.cos(angle), np.sin(angle), 0])
            )
            satelite.move_to(initial_position)

            satelite.add_updater(
                lambda m, dt, i=i, initial_position=initial_position, planeta=planeta: m.move_to(
                    planeta.get_center()
                    + separation
                    * planeta.get_height()
                    * np.array([np.cos(angle + i * dt), np.sin(angle + i * dt), 0])
                )
            )

            satelites.add(satelite)
        return satelites

    def gravity_simulation(self, planetas, satelites, G):
        for satelite in satelites:
            satelite.mass = np.random.uniform(
                1, 3
            )  # Asignar masa aleatoria a cada satélite

        for planeta in planetas:
            planeta.mass = np.random.uniform(
                5, 10
            )  # Asignar masa aleatoria a cada planeta

        for satelite in satelites:
            satelite.velocity = np.zeros(3)

            satelite.add_updater(
                lambda m, dt, satelite=satelite, planetas=planetas: self.apply_gravity(
                    m, dt, satelite, planetas, G
                )
            )

    def apply_gravity(self, satelite, dt, satelite_obj, planetas, G):
        total_force = np.zeros(3)
        for planeta in planetas:
            if satelite_obj != planeta:
                direction = planeta.get_center() - satelite_obj.get_center()
                distance = np.linalg.norm(direction)
                force_magnitude = G * (satelite_obj.mass * planeta.mass) / distance**2
                force = force_magnitude * direction / distance
                total_force += force

        acceleration = total_force / satelite_obj.mass
        velocity_change = acceleration * dt
        satelite.velocity += velocity_change
        satelite.shift(satelite.velocity * dt)
