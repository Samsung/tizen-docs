# Window System

## Overview
The Tizen Window System Hardware Abstraction Layer (HAL) is a critical component that bridges the gap between the high-level window system software and the underlying graphics and display hardware. Its primary purpose is to provide a standardized and consistent interface for window system operations, enabling Tizen to function across a wide variety of hardware configurations with different chipsets and GPUs.

By abstracting the hardware-specific details, the Window System HAL allows the core window system components—such as the client applications and the display server—to interact with graphics and display hardware in a unified manner. This abstraction facilitates hardware rendering, efficient buffer sharing between processes, and organized management of display outputs.

For Tizen to be ported to new hardware, a backend module specific to that hardware must be implemented for the Window System HAL.

## Key Subsystems of the Window System HAL
The Window System HAL is composed of two primary subsystems, each responsible for a distinct set of functionalities:

- **HAL TBM Module (Tizen Buffer Manager)**
- **HAL TDM Module (Tizen Display Manager)**

---

### HAL TBM Module (Tizen Buffer Manager)
The HAL TBM Module provides the hardware abstraction layer for Tizen Buffer Manager (TBM). TBM is the system responsible for allocating, managing, and sharing graphics buffers, which are essential for rendering UI elements and displaying content.

**Key Responsibilities:**
 - **Buffer Allocation and Management:** Provides interfaces for creating and managing graphics memory buffers (e.g., for surfaces, windows, and textures).
 - **Hardware-Specific Backend:** The backend of the HAL TBM Module is inherently hardware-dependent. It implements the actual buffer operations (allocation, locking, unlocking, etc.) using the native capabilities of the target system's GPU and memory management unit.
 - **Inter-Process Buffer Sharing:** Enables efficient sharing of graphics buffers between different processes (e.g., between a client application and the display server). To facilitate this, the HAL TBM Module provides interface of file descriptor (fd) and a key for each buffer, allowing other processes to access the shared graphics memory directly without data duplication.
 - **Unified Interface:** Exposes a consistent API to the upper layers of the window system, regardless of the underlying hardware.

**Implementation Requirement:**
Chipset vendors are required to develop and provide their own backend implementations for the HAL TBM Module. This ensures that TBM can leverage the specific features and optimizations of the target hardware, leading to optimal performance and stability on the Tizen platform.

---

### HAL TDM Module (Tizen Display Manager)

The HAL TDM Module provides the hardware abstraction layer for the Tizen Display Manager (TDM). The display server (e.g., Wayland compositor in Tizen) is responsible for compositing the final image from various client buffers and presenting it on the screen. The HAL TDM Module equips the display server with the necessary tools to control and manage the display hardware effectively.

**Key Responsibilities:**
 - **Display Hardware Resource Management:** Provides the display server with detailed information about available display hardware resources, such as display connectors (HDMI, eDP, DSI), display modes (resolutions, refresh rates), and hardware planes (overlays).
 - **Hardware Composition and Control:** Allows the display server to offload certain compositing tasks directly to the display hardware. For instance, it can instruct the hardware to scale, rotate, or convert the color format of a buffer before it is displayed, reducing the load on the CPU and GPU.
 - **Unified Interface for Diverse Hardware:** Offers a standardized set of APIs for the display server to interact with a wide range of display controllers and chipsets. This allows a single display server implementation to work seamlessly with different hardware.
 - **Mode Setting and Output Configuration:** Manages the configuration of display outputs, including setting the display mode, enabling/disabling outputs, and handling hot-plug events for external displays.

**Purpose:**
The HAL TDM Module is essential for enabling advanced display features and ensuring high-performance graphics rendering. By providing direct access to hardware capabilities, it allows the display server to efficiently manage multiple layers, perform hardware-accelerated post-processing, and adapt to various display panels and connectors.

