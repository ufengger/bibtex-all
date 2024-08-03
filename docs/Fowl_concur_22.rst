Notes on: Fowler, M. (2022): Python Concurrency with asyncio
============================================================

`View on DouBan <https://book.douban.com/subject/35219949/>`_

.. code-block:: bibtex

   @Book{Fowl_concur_22,
     author    = {Fowler, Matthew},
     title     = {Python Concurrency with asyncio},
     year      = 2022,
     publisher = {Manning},
     url       = {https://book.douban.com/subject/35219949/},
   }

What is asyncio?
----------------

**I/O** refers to a computer's input and output devices such as a keyboard, hard
drive, and, most commonly, a network card.

**Concurrency** means allowing more than one task being handled at the same time.
In the case of concurrent I/O, examples include allowing multiple web requests
to be made at the same time or allowing simultaneous connections to a web
server.

*asyncio* is short for *asynchronous I/O*.

So what is asynchronous programming? It means that a particular long-running
task can be run in the background separate from the main application. Instead of
blocking all other application code waiting for that long-running task to be
completed, the system is free to do other work that is not dependent on that
task. Then once the long-running task is completed, we'll be notified that it is
done so we can process the result.

A *coroutine* is a method that can be paused when we have a potentially
long-running task and then resumed when that task is finished.

*asyncio* is a library to execute these coroutines in an asynchronous fashion
using a concurrency model known as a *single-threaded event loop*.

What is I/O-bound and what is CPU-bound?
----------------------------------------

.. list-table:: I/O-bound and CPU-bound

   * - Code
     - bound

   * - ``import request``

   * - ``response = request.get('https://www.example.com')``
     - I/O-bound web request

   * - ``items = response.headers.items()``

   * - ``headers = [f'{key}: {header}' for key, header in items]``
     - CPU-bound response processing

   * - ``formatted_headers = '\n'.join(headers)``
     - CPU-bound string concatenation

   * - ``with open('headers.txt', 'w') as file:``
     - I/O-bound open a file

   * - ``file.write(formatted_headers)``
     - I/O-bound write to disk

Concurrency
~~~~~~~~~~~

When we say two tasks are happening *concurrently*, we mean those tasks are
happening at the same time.

This switching between tasks (doing something else while the oven heats,
switching between two different cakes) is *concurrent* behavior.

Parallelism
~~~~~~~~~~~

When we say something is running *in parallel*, we mean not
only are there two or more tasks happening concurrently,
but they are also executing at the same time.

With *concurrency*, we have multiple tasks happening at
the same time, but only one we're actively doing at a given
point in time. With *parallelism*, we have multiple tasks
happening and are actively doing more than one simultaneously.

The difference between concurrency and parallelism
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Concurrency** is about multiple tasks that can happen
independently from one another. We can have concurrency
on a CPU with only one core, as the operation will employ
*preemptive multitasking* to switch between tasks.

**Parallelism**, however, means that we must be executing two
or more tasks at the same time. On a machine with one core,
this is not possible.

What is multitasking?
~~~~~~~~~~~~~~~~~~~~~

**Preemptive multitasking**

In this model, we let the operating system decide how to
switch between which work is currently being executed via
a process called *time slicing*. When the operating system
switches between work, we call it *preempting*.

**Cooperative multitasking**

In this model, instead of relying on the operating system
to decide when to switch between which work is currently
being executed, we explicitly code points in our application
where we can let other tasks run. The tasks in our
application operate in a model where they *cooperate*,
explicitly saying, "I'm pausing my taskfor a while; go ahead
and run other tasks."

Process
~~~~~~~

If we are on a CPU with only one core, we can still have multiple applications
running simultaneously, through *time slicing*. When an operating system uses time
slicing, it will switch between which process is running automatically after
some amount of time. The algorithms that determine when this switching occurs
are different, depending on the operating system.

Thread
~~~~~~

A process will always have at least one thread associated
with it, usually known as the *main thread*. A process can
also create other threads, which are more commonly known
as *worker* or *background* threads.

Multithreading is only useful for I/O-bound work because
we are limited by the global interpreter lock.

Understanding the global interpreter lock
-----------------------------------------

Briefly, the GIL prevents one Python process from executing
more than one Python bytecode instruction at any given time.
This means that even if we have multiple threads on a machine
with multiple cores, a Python process can have only one thread
running Python code at a time.

*NOTE* Multiprocessing can run multiple bytecode instruction
concurrently because each Python process has its own GIL.

So why does the GIL exist? The answer lies in how memory is
managed in CPython. In CPython, memory is managed primarily
by a process known as *reference counting*. Reference
counting works by keeping track of who currently needs
access to a particular Python object, such as an integer,
dictionary, or list. A reference count is an integer keeping
track of how many places reference that particular object.
When someone no longer needs that referenced object, the
reference count is decremented, and when someone else needs
it, it is incremented. When the reference count reaches zero,
no one is referencing the object, and it can be deleted from
memory.

Is the GIL ever released?
~~~~~~~~~~~~~~~~~~~~~~~~~

The GIL is released when I/O operations happen. This lets us
employ threads to do concurrent work when it comes to I/O,
but not for CPU-bound Python code itself.

So how is it that we can release the GIL for I/O but not for
CPU-bound operations? The answer lies in the system calls
that are made in the background. In the case of I/O, the
low-level system calls are outside of the Python runtime.
This allows the GIL to be released because it is not
interacting with Python objects directly. In this case,
the GIL is only reacquired when the data received is
translated back into a Python object. Then, at the OS
level, the I/O operations execute concurrently. This model
gives us concurrency but not parallelism.

What is a socket?
~~~~~~~~~~~~~~~~~

A *socket* is a low-level abstraction for sending and receiving data over a
network.

Creating coroutines with the async keyword
------------------------------------------

This is an important point, as coroutines aren't exectued when we call them
directly. Instead, we create a coroutine object that can be run later. To run a
coroutine, we need to explicitly run it on an event loop.
